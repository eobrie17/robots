import constants as c
import random
import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p
class MOTOR:
    def __init__(self, joint_name):
        self.joint_name = joint_name
        self.motor_values = np.zeros(c.iterations)
        self.prepare_to_act()
    
    def prepare_to_act(self):
        print(self.joint_name)
        self.amplitude = c.amplitude 
        self.frequency = c.frequency
        self.offset = c.phaseOffset
        x = np.linspace(0, 2*np.pi, c.iterations)
        if str(self.joint_name) == "b'Torso_FrontLeg'":
            self.motor_values = self.amplitude * np.sin(self.frequency/2 * x + self.offset)
        else:
            self.motor_values = self.amplitude * np.sin(self.frequency * x + self.offset)

    def set_value(self, robot, time):
        pyrosim.Set_Motor_For_Joint(

            bodyIndex = robot,

            jointName = self.joint_name,

            controlMode = p.POSITION_CONTROL,

            targetPosition =  self.motor_values[time],

            maxForce = 500)

    def save_values(self):
        np.save('data/motorvals.npy', self.motor_values)