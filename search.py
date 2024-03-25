import os
from hillclimber import HILLCLIMBER 


# os.system("python3 generate.py")
# os.system("python3 simulate.py")

hc = HILLCLIMBER()
hc.evolve()
hc.show_best()