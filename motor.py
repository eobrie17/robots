import constants as c
import random
import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p
class MOTOR:
    def __init__(self, joint_name):
        self.joint_name = joint_name
        self.motor_values = np.zeros(c.iterations)

    def set_value(self, robot, desiredAngle):
        pyrosim.Set_Motor_For_Joint(

            bodyIndex = robot,

            jointName = self.joint_name,

            controlMode = p.POSITION_CONTROL,

            targetPosition =  desiredAngle,

            maxForce = 500)
