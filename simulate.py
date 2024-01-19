import pybullet as p
import time

physicsClient = p.connect(p.GUI)
#this disables the sidebars
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

for i in range(0, 1000):
    p.stepSimulation()
    time.sleep(1/60)
    print(i)

p.disconnect()