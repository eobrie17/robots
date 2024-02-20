import numpy as np
import matplotlib.pyplot as plt

backLegSensorValues = np.load('data/backLegTouch.npy')
frontLegSensorValues = np.load('data/frontLegTouch.npy')

bLtargetAngles = np.load('data/backLegAngles.npy')
fLtargetAngles = np.load('data/frontLegAngles.npy')

plt.plot(bLtargetAngles, label='Back Leg Target Angles')
plt.plot(fLtargetAngles, label='Front Leg Target Angles')
plt.xlabel('Angle [rad]')
plt.ylabel('sin(x)')
plt.axis('tight')
plt.show()

# plt.plot(backLegSensorValues, label='Back Leg Sensor Values', linewidth=3)
# plt.plot(frontLegSensorValues, label='Front Leg Sensor Values')
# plt.legend()
# plt.show()