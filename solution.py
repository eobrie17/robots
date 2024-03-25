import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random

class SOLUTION:
    def __init__(self):
        self.weights = np.random.rand(3, 2) * 2 - 1

    def evaluate(self, directOrGUI):
        self.create_world()
        self.create_body()
        self.create_brain()

        os.system(f"python3 simulate.py {directOrGUI}")

        fitnessFile = 'fitness.txt'
        with open(fitnessFile, 'r') as file:
            self.fitness = float(file.read())

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
        pyrosim.Start_NeuralNetwork("brain.nndf")
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
        