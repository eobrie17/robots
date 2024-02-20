import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np 
import random

bLamplitude = np.pi/6
bLfrequency = 7
bLphaseOffset = np.pi/4
fLamplitude = np.pi/6
fLfrequency = 7
fLphaseOffset = 0


physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

#this disables the sidebars
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")

robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

iterations = 1000

backLegSensorValues = np.zeros(iterations)
frontLegSensorValues = np.zeros(1000)

bLx = np.linspace(0, 2*np.pi, iterations)
bLtargetAngles = bLamplitude * np.sin(bLfrequency * bLx + bLphaseOffset)

fLx = np.linspace(0, 2*np.pi, iterations)
fLtargetAngles = fLamplitude * np.sin(fLfrequency * fLx + fLphaseOffset)

np.save('data/backLegAngles.npy', bLtargetAngles)
np.save('data/frontLegAngles.npy', fLtargetAngles)


for i in range(0, iterations):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(

        bodyIndex = robotId,

        jointName = b"Torso_BackLeg",

        controlMode = p.POSITION_CONTROL,

        targetPosition =  random.uniform(bLtargetAngles[i],bLtargetAngles[i]),

        maxForce = 500)
    pyrosim.Set_Motor_For_Joint(

        bodyIndex = robotId,

        jointName = b"Torso_FrontLeg",

        controlMode = p.POSITION_CONTROL,

        targetPosition =  random.uniform(fLtargetAngles[i], fLtargetAngles[i]),

        maxForce = 500)
    time.sleep(1/1000)


p.disconnect()

np.save('data/backLegTouch.npy', backLegSensorValues )
np.save('data/frontLegTouch.npy', frontLegSensorValues )
