import os
from hillclimber import HILLCLIMBER 
from parallelHillClimber import PARALLEL_HILLCLIMBER


# os.system("python3 generate.py")
# os.system("python3 simulate.py")

phc = PARALLEL_HILLCLIMBER()
phc.evolve()
phc.show_best()