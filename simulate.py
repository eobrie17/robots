import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np 
import random
import constants as c
from simulation import SIMULATION

simulation = SIMULATION()




# backLegSensorValues = np.zeros(c.iterations)
# frontLegSensorValues = np.zeros(1000)

# bLx = np.linspace(0, 2*np.pi, c.iterations)
# bLtargetAngles = c.bLamplitude * np.sin(c.bLfrequency * bLx + c.bLphaseOffset)

# fLx = np.linspace(0, 2*np.pi, c.iterations)
# fLtargetAngles = c.fLamplitude * np.sin(c.fLfrequency * fLx + c.fLphaseOffset)

# np.save('data/backLegAngles.npy', bLtargetAngles)
# np.save('data/frontLegAngles.npy', fLtargetAngles)


# for i in range(0, c.iterations):
#     p.stepSimulation()
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#     pyrosim.Set_Motor_For_Joint(

#         bodyIndex = robotId,

#         jointName = b"Torso_BackLeg",

#         controlMode = p.POSITION_CONTROL,

#         targetPosition =  random.uniform(bLtargetAngles[i],bLtargetAngles[i]),

#         maxForce = 500)
#     pyrosim.Set_Motor_For_Joint(

#         bodyIndex = robotId,

#         jointName = b"Torso_FrontLeg",

#         controlMode = p.POSITION_CONTROL,

#         targetPosition =  random.uniform(fLtargetAngles[i], fLtargetAngles[i]),

#         maxForce = 500)
#     time.sleep(1/1000)


# p.disconnect()

# np.save('data/backLegTouch.npy', backLegSensorValues )
# np.save('data/frontLegTouch.npy', frontLegSensorValues )
