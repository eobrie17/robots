import pybullet as p
import pyrosim.pyrosim as pyrosim
import os
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import constants as c

class ROBOT:
    def __init__(self, solutionID):
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK(f"brain{solutionID}.nndf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.prepare_to_sense()
        self.prepare_to_act()
        self.solutionID = solutionID
        os.system(f"rm brain{self.solutionID}.nndf")

    
    def prepare_to_sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def sense(self, time):
        for sensor in self.sensors.values():
            sensor.get_value(time)

    def prepare_to_act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def act(self, desiredAngle):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                # extract the name of the joint to which this motor neuron connects
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName).encode('ASCII')
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].set_value(self.robotId, desiredAngle)
                # print('neuron name: ', neuronName)
                # print('joint name: ', jointName)
                # print('motor neuron value: ', desiredAngle)


    def think(self, time):
        self.nn.Update()
        #self.nn.Print()
    
    def get_fitness(self, time):
        stateOfLinkZero = p.getLinkState(self.robotId,0)
        positionOfLinkZero = stateOfLinkZero[0]
        #xCoordinateOfLinkZero = positionOfLinkZero[0]
        x, y, z = positionOfLinkZero

        #velocity = y
        distance = (x**2 + y**2 + z**2)**0.5  # Distance from the origin
        speed = distance / time

        #write to speed file 
        f1 = open("speeds.txt", "a")
        f1.write(str(speed)+ "\n")
        f1.close()
        
        #write to fitness file
        f2 = open(f"tmp{self.solutionID}.txt", "w")
        os.system(f"mv tmp{self.solutionID}.txt fitness{self.solutionID}.txt")
        f2.write(str(distance))
        f2.close()
        