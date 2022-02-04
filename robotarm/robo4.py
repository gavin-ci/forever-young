from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

for i in range(3, 0, -1):
    robotArm.grab()
    for x in range(i):
        robotArm.moveRight()
    robotArm.drop()
    if i == 1:
        break
    for x in range(i):
        robotArm.moveLeft()
    
for i in range(1, 3):
    for x in range(i):
        robotArm.moveRight()
    robotArm.grab()
    for x in range(i):
        robotArm.moveLeft()
    robotArm.drop()

robotArm.speed = 3
robotArm.wait()