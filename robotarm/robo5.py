from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

for i in range(7):
    robotArm.moveRight()

for i in range(8):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.moveLeft()

robotArm.speed = 2
robotArm.wait()