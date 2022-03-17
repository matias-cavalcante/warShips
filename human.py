

class Human():

    def chooseHumanShip(self):
        choice = input("Type 'l' for Light-Ship, or 'h' for Heavy-Ship: ")
        if choice == 'l':
            return True
        elif choice == 'h':
            return False

    def humanMoves(self, currently):
        position = input("Press 'l' to move left, or 'r' to move right: ")
        if position == 'l':
            position = currently - 1
            if position == 0:
                position = 3
        elif position == 'r':
            position = currently + 1
            if position == 4:
                position = 1
        return position

    # Maybe this is what i want. Check well later
    def humanSelectAction(self, selfPosition):
        action = input("Press 's' to shoot, or 'm' to move: ")
        if action == 's':
            return True
        else:
            False
