# import random number
from random import randint


def welcome():
    """
    Prints welcome message to player
    """
    print(" Welcome to BATTLESHIP\n")


def rules(user):
    """
    describes rules for each game type
    """
    print(f"\n {user.name} you are at WAR! \n"
          " Battle the enemy and sink their ships\n\n"
          " Game 1 rules: \n"
          " You have 12 shots to sink the enemy ships to win the war \n \n"
          " Game 2 rules: \n"
          " You and the enemy will take turns firing at each other's ships \n"
          " First one to sink them all will win the war \n")


def validate_data(data, data_list):
    """
    function to validate player input
    """
    try:
        if data not in data_list:
            raise ValueError(
                f"Please choose : {' '.join(data_list)}")
    except ValueError as e:
        print(f" Invalid entry. {e}")
        return False
    return True


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
        print(" Ok Captain what is your name? \n")
        user_name = input(" \n")
        if user_name == "":
            user_name = "lazy bones"
        self.name = user_name.upper()
        return self.name

    def size_choices(self):
        """
        Gets user input for grid size
        validates input
        uses input to alocate players size
        returns size
        """
        grids = ["4", "5", "6", "7", "8", ""]
        while True:
            print(" Pick your battlefield grid size:\n")
            choice = input(" 4 5 6 7 or 8? \n")
            if validate_data(choice, grids):
                break
        if choice == "":
            print("Ok The computer will pick for you\n")
            self.size = randint(4, 8)
            return self.size
        print(f" You picked battlefield grid size {choice}\n")
        self.size = int(choice)
        return self.size


def main():
    """
    runs the whole game
    """
    welcome()
    user = Player("", 0, 0)
    Player.get_user_name(user)
    rules(user)
    Player.size_choices(user)


main()
