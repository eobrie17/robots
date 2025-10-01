
from solution import SOLUTION
import copy
import numpy as np
import constants as c

class HILLCLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def evolve(self):
        self.parent.evaluate('GUI')
        for currentGeneration in range(c.numberOfGenerations):
            self.evolve_for_one_generation()
    
    def evolve_for_one_generation(self):
        self.spawn()
        self.mutate()
        self.child.evaluate('DIRECT')
        self.print()
        self.select()
    
    def spawn(self):
        self.child = copy.deepcopy(self.parent)

    def mutate(self):
        self.child.mutate()

    def select(self):
        #if parent does worse, replace it with the child
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def print(self):
        print(f"parent fitness: {self.parent.fitness}, child fitness: {self.child.fitness}")

    def show_best(self):
        self.parent.evaluate('GUI')