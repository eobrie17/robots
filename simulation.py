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
        for i in range(0, c.iterations):
            p.stepSimulation()
            self.robot.sense(i)
            self.robot.think(i)
            self.robot.act(i)
            if self.directOrGUI == "GUI":
                time.sleep(1/1800)

    def get_fitness(self):
        self.robot.get_fitness()
        
    def __del__(self):
        p.disconnect()
