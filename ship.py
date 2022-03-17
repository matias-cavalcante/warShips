
from doctest import testsource
from imghdr import tests


class Ships:
    def __init__(self, shipy):
        if shipy == True:  # True for light ship
            self.shield = 65
            self.firePower = 70
            self.engine = 40
            self.life = 100
        elif shipy == False:  # False for heavy shipS
            self.shield = 85
            self.firePower = 65
            self.engine = 20
            self.life = 100

    def setShield(self, points):
        self.shield = points

    def setFirePower(self, points):
        self.firePower = points

    def setEngine(self, points):
        self.engine = points

    def setLife(self, points):
        self.life = points

    def move(position):
        if position == 'l':
            return True
        else:
            return False


"""
testShip = Ships(False)

print(testShip.shield)

testShip.setShield(50)

print("Now see ", testShip.shield)
"""
