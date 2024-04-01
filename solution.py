import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time

class SOLUTION:
    def __init__(self, id):
        self.weights = np.random.rand(3, 2) * 2 - 1
        self.myID = id

    # def evaluate(self, directOrGUI):
    #     self.create_world()
    #     self.create_body()
    #     self.create_brain()

    #     #search.py will continue to run without waiting for simulate.py to finish
    #     os.system(f"python3 simulate.py {directOrGUI} {self.myID} &")

    #     while not os.path.exists(fitnessFileName):
    #         time.sleep(0.01)

    #     fitnessFile = f'fitness{self.myID}.txt'
    #     with open(fitnessFile, 'r') as file:
    #         self.fitness = float(file.read())

    def start_simulation(self, directOrGUI):
        self.create_world()
        self.create_body()
        self.create_brain()

        #search.py will continue to run without waiting for simulate.py to finish
        os.system(f"python3 simulate.py {directOrGUI} {self.myID} 2&>1 &")

    def wait_for_simulation_to_end(self):
        fitnessFile = f'fitness{self.myID}.txt'

        while not os.path.exists(fitnessFile):
            time.sleep(0.8)

        with open(fitnessFile, 'r') as file:
            self.fitness = float(file.read())

        os.system(f"rm fitness{self.myID}.txt")

    def create_world(self):
        pyrosim.Start_SDF("world.sdf")
        length = 1
        width = 1
        height = 1
        x=5
        y=0
        z=.5
        pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length, width, height])
        pyrosim.End()


    def create_body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5], size=[1, 1, 1])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-.5,0,-.5], size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2,0,1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[.5,0,-.5], size=[1,1,1])
        pyrosim.End()

    def create_brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")
        #sensor neurons receive values from sensors
        #name our neurons with numbers, because we are going to update the values\
        #of each neuron in our neural network, every simulation time step, in a specific order:\
        # sensor neurons first, hidden neurons next, and finally motor neurons

        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

        for currentRow in range(3):
            for currentColumn in range(1):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn + 3 , weight = self.weights[currentRow][currentColumn])

        pyrosim.End()
    
    def mutate(self):
        randomRow = random.randint(0,2)
        randomCol = random.randint(0,1)
        #random element
        self.weights[randomRow, randomCol] = random.random()*2-1
    
    def set_ID(self, nextAvailableID):
        self.myID = nextAvailableID
        
        