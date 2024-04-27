
from solution import SOLUTION
import copy
import numpy as np
import constants as c
import os
import matplotlib.pyplot as plt

class PARALLEL_HILLCLIMBER:
    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        os.system("rm speeds.txt")
        self.nextAvailableID = 0
        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        

    def evolve(self):
        self.evaluate(self.parents)
        # self.parent.evaluate('GUI')
        for currentGeneration in range(c.numberOfGenerations):
            self.evolve_for_one_generation()
    
    def evolve_for_one_generation(self):
        self.spawn()
        self.mutate()
        self.evaluate(self.children)
        self.print_fitness()
        self.select()
    
    def spawn(self):
        self.children = {}
        for item, value in self.parents.items():
            self.children[item] = copy.deepcopy(value)
            self.children[item].set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def mutate(self):
        for name, solution in self.children.items():
            solution.mutate()

    def evaluate(self, solutions):
        #solutions is either self.parents or self.children
        for i in range(c.populationSize):
            solutions[i].start_simulation('DIRECT')
        
        for i in range(c.populationSize):
            solutions[i].wait_for_simulation_to_end()
            #print('fitness: ', self.parents[i].fitness)

    def select(self):
        for key in self.parents.keys():
            if self.parents[key].fitness < self.children[key].fitness:
                self.parents[key] = self.children[key]

    def print_fitness(self):
        for key in self.parents.keys():
            print(f"\nparent fitness: {self.parents[key].fitness}, child fitness: {self.children[key].fitness}\n")
    
    def graph_speeds(self):
        with open('speeds.txt', 'r') as file:
            #list of speeds stripped
            speed_data = [line.strip() for line in file.readlines()]
        #make sure they are floats
        speeds_float = [float(speed) for speed in speed_data]

        plt.figure(figsize=(10, 5))
        plt.plot(speeds_float, marker='o', linestyle='-', color='b') 
        plt.title('Robot Speeds Throughout Evolution')  
        plt.xlabel('Number of Robots Generated')  
        plt.ylabel('Speed (any direction)')  
        plt.grid(True) 
        #marker for each generation (10 robots per generation)
        num_robots = len(speeds_float)
        for i in range(10, num_robots, 10):
            plt.axvline(x=i, color='r', linestyle='--', linewidth=1)
        plt.show()


    #TODO pick so we display parent with the lowest fitness score!!
    def show_best(self):
        best_fitness = -10000000000
        for name, solution in self.parents.items():
            print(f"Checking solution {name} with fitness {solution.fitness}")  # Debug output
            if solution.fitness > best_fitness:
                best_solution = solution
                best_fitness = solution.fitness
                print(f"New best found: {name} with fitness {best_fitness}") 
        print("BEST------- ", best_solution.fitness)
        best_solution.start_simulation("GUI")
        self.graph_speeds()