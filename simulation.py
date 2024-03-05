import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from world import WORLD
from robot import ROBOT
import constants as c
import time

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        p.setGravity(0,0,-9.8)

        self.world = WORLD()
        self.robot = ROBOT()



    def run(self):
        for i in range(0, c.iterations):
            p.stepSimulation()
            self.robot.sense(i)
            self.robot.think(i)
            self.robot.act(i)
            time.sleep(1/1100)
        
    def __del__(self):
        p.disconnect()