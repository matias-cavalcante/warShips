from random import randint

# So MACHINE will have to make same moves as human, just in through a differente process


class Machine():
    def selectMachineShip(self):
        choice = randint(0, 1)
        if choice == 0:
            return True
        else:
            return False

    def machineMoves(self, currently):
        position = randint(1, 2)  # l & r
        if position == 1:
            position = currently - 1
            if position == 0:
                position = 3
        elif position == 2:
            position = currently + 1
            if position == 4:
                position = 1
        return position
