import numpy as np
import matplotlib.pyplot as plt

backLegSensorValues = np.load('data/backLegTouch.npy')
frontLegSensorValues = np.load('data/frontLegTouch.npy')

plt.plot(backLegSensorValues, label='Back Leg Sensor Values', linewidth=3)
plt.plot(frontLegSensorValues, label='Front Leg Sensor Values')
plt.legend()
plt.show()