from random import randint
from ship import Ships
from human import Human
import machine


def shootingHitOrNot(positionH, positionM):
    if positionH == positionM:
        return True
    else:
        return False


def machineManager(machineLife, humanLife):
    randomChoice = randint(0, 3)
    if randomChoice == 2:
        return False
    return True


def main():
    humanMethods = Human()
    machineMethods = machine.Machine()

    humanShipChoice = humanMethods.chooseHumanShip()
    humanShip = Ships(humanShipChoice)

    machineShipChoice = machineMethods.selectMachineShip()
    machineShip = Ships(machineShipChoice)

    humanPosition = randint(1, 3)
    machinePosition = randint(1, 3)

    print("Machine power ---> ", machineShip.firePower)
    print("Human power ---> ", humanShip.firePower)

    while humanShip.life > 1 and machineShip.life > 1:  # WHILE BOTH PLAYERS ARE ALIVE
        methodChosen = humanMethods.humanSelectAction(
            machinePosition)
        if methodChosen == True:
            methodChosen = humanShip.firePower
            impact = shootingHitOrNot(humanPosition, machinePosition)
            print()
            if impact == True:
                if machineShip.shield >= methodChosen:
                    machineShip.setShield(machineShip.shield - methodChosen)
                elif machineShip.shield == 65 and methodChosen == 65:
                    machineShip.setShield(0)
                elif machineShip.shield <= 65 and methodChosen > 65:
                    lifeImpact = methodChosen - machineShip.shield
                    machineShip.setShield(0)
                    machineShip.setLife(machineShip.life - lifeImpact)
                elif machineShip.life > 0 and machineShip.life > methodChosen:
                    machineShip.setLife(machineShip.life - methodChosen)
                elif machineShip.life > 0 and machineShip.life <= methodChosen:
                    machineShip.setLife(0)
                    print("H-U-M-A-N W-I-N-S!")
        elif methodChosen != True:  # 'l' or 'r'
            humanPosition = humanMethods.humanMoves(humanPosition)

        humanLifeLastValue = humanShip.life
        determineMachineAction = machineManager(
            machineShip.life, humanLifeLastValue)

        if determineMachineAction == True:
            print("H SHIELD -- ", humanShip.shield)
            print("H LIFE -- ", humanShip.life)
            print()
            machineMethodChosen = machineShip.firePower
            impacto = shootingHitOrNot(humanPosition, machinePosition)
            print("Machine P --> ", machinePosition)
            print(" Human P -->", humanPosition)
            print()
            if impacto == True:
                print("Human HITTED")
                if humanShip.shield > machineMethodChosen:
                    humanShip.setShield(humanShip.shield - machineMethodChosen)
                elif humanShip.shield == 0 and humanShip.life < machineMethodChosen:
                    humanShip.setLife(0)
                    print("Human destroyed")
                    break
                elif humanShip.shield == machineMethodChosen:
                    humanShip.setShield(0)
                elif humanShip.shield == 65 and machineMethodChosen > humanShip.shield or machineMethodChosen > humanShip.shield:
                    takeFromLife = machineMethodChosen - humanShip.shield
                    humanShip.setShield(0)
                    humanShip.setLife(100 - takeFromLife)
                elif humanShip.shield == 0 and humanShip.life > machineMethodChosen:
                    humanShip.setLife(humanShip.life - machineMethodChosen)

        elif determineMachineAction == False:  # 'l' or 'r'
            machinePosition = machineMethods.machineMoves(machinePosition)
        print("HUMAN SHIELD: ", humanShip.shield)
        print("HUMAN LIFE: ", humanShip.life)
        print("HUMAN POSITION: ", humanPosition)
        print()
        print("MACHINE SHIELD: ", machineShip.shield)
        print("MACHINE LIFE: ", machineShip.life)
        print("MACHINE POSITION: ", machinePosition)

    return "Game over "

    # Now machine
main()
