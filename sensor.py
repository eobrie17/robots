import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, link_name):
        self.link_name = link_name
        self.values = np.zeros(c.iterations)

    def get_value(self, time):
        self.values[time] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.link_name)
        if time == c.iterations:
            print(self.values)
    
    def save_values(self):
        np.save('data/sensorvals.npy', self.values)