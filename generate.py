import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

length = 1
width = 1
height = 1

x=0
y=0
z=.5

#columns
for i in range(5):
    #rows
    for j in range(5):
        #this creates a tower
        for i in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length, width, height])
            z += 1
            length *= .9
            width *= .9
            height *= .9
        x += 1
        #reset tower dimensions
        length = 1
        width = 1
        height = 1
        z = .5
    #reset rows
    x=0
    y += 1



pyrosim.End()


