import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from world import WORLD
from robot import ROBOT
import constants as c
import time

class SIMULATION:
    def __init__(self, directOrGUI, solutionID):

        self.directOrGUI = directOrGUI

        if directOrGUI == 'DIRECT':
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        p.setGravity(0,0,-9.8)

        self.world = WORLD()
        self.robot = ROBOT(solutionID)



    def run(self):
        #i is the time
        for i in range(0, c.iterations):
            self.time = i
            p.stepSimulation()
            self.robot.sense(self.time)
            self.robot.think(self.time)
            self.robot.act(self.time)
            if self.directOrGUI == "GUI":
                time.sleep(1/1800)

    def get_fitness(self):
        self.robot.get_fitness(self.time)
        
    def __del__(self):
        p.disconnect()
