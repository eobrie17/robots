import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:
    def __init__(self, id):
        self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons) * 2 - 1
        self.myID = id

    def start_simulation(self, directOrGUI):
        self.create_world()
        #CHANGE THESE FOR OCTOPOD VS QUADRUPED
        self.create_body_octopod()
        self.create_brain_octopod()

        #search.py will continue to run without waiting for simulate.py to finish
        os.system(f"python3 simulate.py {directOrGUI} {self.myID} 2&>1 &")

    def wait_for_simulation_to_end(self):
        fitnessFile = f'fitness{self.myID}.txt'

        while not os.path.exists(fitnessFile):
            time.sleep(1.5)

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


    def create_body_octopod(self):
        pyrosim.Start_URDF("body.urdf")
        #TORSO
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1], size=[1, 1, 1], mass=1.5)
       
        #FRONT LEG L
        pyrosim.Send_Joint( name = "Torso_FrontLegL" , parent= "Torso" , child = "FrontLegL" , type = "revolute", position = [-.2,0.5,1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLegL", pos=[-.2, 0.5, 0], size=[.2,1,.2], mass=.5)
        pyrosim.Send_Joint( name = "FrontLegL_FrontLowerLegL" , parent= "FrontLegL" , child = "FrontLowerLegL" , type = "revolute", position = [0,1,0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLegL", pos=[-.2, 0, -.5], size=[.2,.2,1], mass=.5)
        #FRONT LEG R
        pyrosim.Send_Joint( name = "Torso_FrontLegR" , parent= "Torso" , child = "FrontLegR" , type = "revolute", position = [.2,0.5,1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLegR", pos=[.2, 0.5, 0], size=[.2,1,.2], mass=.5)
        pyrosim.Send_Joint( name = "FrontLegR_FrontLowerLegR" , parent= "FrontLegR" , child = "FrontLowerLegR" , type = "revolute", position = [0,1,0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLegR", pos=[.2, 0, -.5], size=[.2,.2,1], mass=.5)

        #RIGHT LEG L
        pyrosim.Send_Joint( name = "Torso_RightLegL" , parent= "Torso" , child = "RightLegL" , type = "revolute", position = [.5,-.2,1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLegL", pos=[.5, -.2, 0], size=[1,.2,.2], mass=.5)
        pyrosim.Send_Joint( name = "RightLegL_RightLowerLegL" , parent= "RightLegL" , child = "RightLowerLegL" , type = "revolute", position = [1,0,0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLowerLegL", pos=[0, -.2, -.5], size=[.2,.2,1], mass=.5)
        #RIGHT LEG R
        pyrosim.Send_Joint( name = "Torso_RightLegR" , parent= "Torso" , child = "RightLegR" , type = "revolute", position = [.5,.2,1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLegR", pos=[.5, .2, 0], size=[1,.2,.2], mass=.5)
        pyrosim.Send_Joint( name = "RightLegR_RightLowerLegR" , parent= "RightLegR" , child = "RightLowerLegR" , type = "revolute", position = [1,0,0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLowerLegR", pos=[0, .2, -.5], size=[.2,.2,1], mass=.5)

        #BACK LEG L
        pyrosim.Send_Joint( name = "Torso_BackLegL" , parent= "Torso" , child = "BackLegL" , type = "revolute", position = [-.2,-.5,1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLegL", pos=[-.2,-.5,0], size=[.2,1,.2], mass=.5)
        pyrosim.Send_Joint( name = "BackLegL_BackLowerLegL" , parent= "BackLegL" , child = "BackLowerLegL" , type = "revolute", position = [0,-1,0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLowerLegL", pos=[-.2, 0, -.5], size=[.2,.2,1], mass=.5)
        #BACK LEG R
        pyrosim.Send_Joint( name = "Torso_BackLegR" , parent= "Torso" , child = "BackLegR" , type = "revolute", position = [.2,-.5,1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLegR", pos=[.2,-.5,0], size=[.2,1,.2], mass=.5)
        pyrosim.Send_Joint( name = "BackLegR_BackLowerLegR" , parent= "BackLegR" , child = "BackLowerLegR" , type = "revolute", position = [0,-1,0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLowerLegR", pos=[.2, 0, -.5], size=[.2,.2,1], mass=.5)

        #LEFT LEG L
        pyrosim.Send_Joint( name = "Torso_LeftLegL" , parent= "Torso" , child = "LeftLegL" , type = "revolute", position = [-.5,-.2,1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLegL", pos=[-.5, -.2, 0], size=[1,.2,.2], mass=.5)
        pyrosim.Send_Joint( name = "LeftLegL_LeftLowerLegL" , parent= "LeftLegL" , child = "LeftLowerLegL" , type = "revolute", position = [-1,0,0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLegL", pos=[0, -.2, -.5], size=[.2,.2,1], mass=.5)
        #LEFT LEG R
        pyrosim.Send_Joint( name = "Torso_LeftLegR" , parent= "Torso" , child = "LeftLegR" , type = "revolute", position = [-.5,.2,1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLegR", pos=[-.5, .2, 0], size=[1,.2,.2], mass=.5)
        pyrosim.Send_Joint( name = "LeftLegR_LeftLowerLegR" , parent= "LeftLegR" , child = "LeftLowerLegR" , type = "revolute", position = [-1,0,0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLegR", pos=[0, .2, -.5], size=[.2,.2,1], mass=.5)

        pyrosim.End()


    def create_brain_octopod(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")
        #sensor neurons receive values from sensors
        #name our neurons with numbers, because we are going to update the values\
        #of each neuron in our neural network, every simulation time step, in a specific order:\
        # sensor neurons first, hidden neurons next, and finally motor neurons

        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")

        #FRONT LEG
        #left
        pyrosim.Send_Motor_Neuron( name = 1 , jointName = "Torso_FrontLegL")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLegL")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "FrontLegL_FrontLowerLegL")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "FrontLowerLegL")
        #right
        pyrosim.Send_Motor_Neuron( name = 5 , jointName = "Torso_FrontLegR")
        pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "FrontLegR")
        pyrosim.Send_Motor_Neuron( name = 7 , jointName = "FrontLegR_FrontLowerLegR")
        pyrosim.Send_Sensor_Neuron(name = 8, linkName = "FrontLowerLegR")
        
        #RIGHT LEG
        #right
        pyrosim.Send_Motor_Neuron( name = 9, jointName = "Torso_RightLegR")
        pyrosim.Send_Sensor_Neuron(name = 10, linkName = "RightLegR")
        pyrosim.Send_Motor_Neuron( name = 11 , jointName = "RightLegR_RightLowerLegR")
        pyrosim.Send_Sensor_Neuron(name = 12, linkName = "RightLowerLegR")
        #left
        pyrosim.Send_Motor_Neuron( name = 13, jointName = "Torso_RightLegL")
        pyrosim.Send_Sensor_Neuron(name = 14, linkName = "RightLegL")
        pyrosim.Send_Motor_Neuron( name = 15 , jointName = "RightLegL_RightLowerLegL")
        pyrosim.Send_Sensor_Neuron(name = 16, linkName = "RightLowerLegL")

        #BACK LEG
        pyrosim.Send_Motor_Neuron( name = 17 , jointName = "Torso_BackLegL")
        pyrosim.Send_Sensor_Neuron(name = 18, linkName = "BackLegL")
        pyrosim.Send_Motor_Neuron( name = 19, jointName = "BackLegL_BackLowerLegL")
        pyrosim.Send_Sensor_Neuron(name = 20, linkName = "BackLowerLegL")
        #left
        pyrosim.Send_Motor_Neuron( name = 21 , jointName = "Torso_BackLegR")
        pyrosim.Send_Sensor_Neuron(name = 22, linkName = "BackLegR")
        pyrosim.Send_Motor_Neuron( name = 23, jointName = "BackLegR_BackLowerLegR")
        pyrosim.Send_Sensor_Neuron(name = 24, linkName = "BackLowerLegR")

        #LEFT LEG
        pyrosim.Send_Motor_Neuron( name = 25 , jointName = "Torso_LeftLegL")
        pyrosim.Send_Sensor_Neuron(name = 26, linkName = "LeftLegL")
        pyrosim.Send_Motor_Neuron( name = 27 , jointName = "LeftLegL_LeftLowerLegL")
        pyrosim.Send_Sensor_Neuron(name = 28, linkName = "LeftLowerLegL")
        #right
        pyrosim.Send_Motor_Neuron( name = 29 , jointName = "Torso_LeftLegR")
        pyrosim.Send_Sensor_Neuron(name = 30, linkName = "LeftLegR")
        pyrosim.Send_Motor_Neuron( name = 31 , jointName = "LeftLegR_LeftLowerLegR")
        pyrosim.Send_Sensor_Neuron(name = 32, linkName = "LeftLowerLegR")


        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn + c.numSensorNeurons , weight = self.weights[currentRow][currentColumn])

        pyrosim.End()

    def create_body_quadruped(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1], size=[1, 1, 1], mass=1.5)
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,-.5,1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-.5,0], size=[.2,1,.2], mass=.5)
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,0.5,1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[.2,1,.2], mass=.5)
        pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-.5,0,1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-.5, 0, 0], size=[1,.2,.2], mass=.5)
        pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [.5,0,1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[.5, 0, 0], size=[1,.2,.2], mass=.5)
        pyrosim.Send_Joint( name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = [0,1,0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -.5], size=[.2,.2,1], mass=.5)
        pyrosim.Send_Joint( name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = [0,-1,0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -.5], size=[.2,.2,1], mass=.5)
        pyrosim.Send_Joint( name = "LeftLeg_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" , type = "revolute", position = [-1,0,0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -.5], size=[.2,.2,1], mass=.5)
        pyrosim.Send_Joint( name = "RightLeg_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" , type = "revolute", position = [1,0,0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -.5], size=[.2,.2,1], mass=.5)
        pyrosim.End()

    def create_brain_quadruped(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")
        #sensor neurons receive values from sensors
        #name our neurons with numbers, because we are going to update the values\
        #of each neuron in our neural network, every simulation time step, in a specific order:\
        # sensor neurons first, hidden neurons next, and finally motor neurons

        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")
        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "RightLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 11 , jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron( name = 12 , jointName = "Torso_RightLeg")
        pyrosim.Send_Motor_Neuron( name = 13 , jointName = "FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 14 , jointName = "BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 15 , jointName = "LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 16 , jointName = "RightLeg_RightLowerLeg")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn + c.numSensorNeurons , weight = self.weights[currentRow][currentColumn])

        pyrosim.End()
    
    def mutate(self):
        randomRow = random.randint(0,c.numSensorNeurons - 1)
        randomCol = random.randint(0, c.numMotorNeurons - 1)
        #random element
        self.weights[randomRow, randomCol] = random.random()*2-1
    
    def set_ID(self, nextAvailableID):
        self.myID = nextAvailableID
        
        