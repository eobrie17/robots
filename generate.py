import pyrosim.pyrosim as pyrosim

def create_world():
    pyrosim.Start_SDF("world.sdf")
    length = 1
    width = 1
    height = 1
    x=3
    y=0
    z=.5
    pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length, width, height])
    pyrosim.End()

def create_robot():
    pyrosim.Start_URDF("body.urdf")
    length = 1
    width = 1
    height = 1
    x=0
    y=0
    z=.5
    pyrosim.Send_Cube(name="Torso", pos=[x,y,z] , size=[length, width, height])
    pyrosim.End()

create_world()
create_robot()


