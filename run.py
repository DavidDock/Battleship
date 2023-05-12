# import random number
from random import randint


def welcome():
    """
    Prints welcome message to player
    """
    print(" Welcome to BATTLESHIP\n")


class Player:
    """
    class for player with methods to
    get name, grid size and  number of ships
    """

    def __init__(self, name, size, ships):
        """
        create player
        """
        self.name = name
        self.size = size
        self.ships = ships

    def get_user_name(self):
        """
        Gets user input for their name
        uses input to name player
        returns name
        """
        print("Ok Captain what is your name? \n")
        user_name = input("\n")
        if user_name == "":
            user_name = "lazy bones"
        self.name = user_name.upper()
        print(f"\nHello {self.name}\n")
        return self.name


def main():
    """
    runs the whole game
    """
    welcome()
    user = Player("", 0, 0)
    Player.get_user_name(user)


main()
