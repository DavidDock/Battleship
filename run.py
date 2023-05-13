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


def choose_game():
    """
    get player to choose game type
    validate input
    return choice
    """
    game_choices = ["1", "2"]
    while True:
        print(" Pick your Game:")
        game_pick = input(" 1 or 2? \n")
        if validate_data(game_pick, game_choices):
            break
    print(f"\n You picked Game {game_pick} \n")
    return game_pick


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

    def size_choice(self):
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

    def ships_choice(self):
        """
        get user to choose amount of ships
        validate input
        uses input to alocate ships to player
        returns ships
        """
        ship_number = ["1", "2", "3", "4", "5", "6", "7", "8", ""]
        while True:
            print(" Pick the number of Ships: ")
            choice_ships = input(" 1 2 3 4 5 6 or 8?\n")
            if validate_data(choice_ships, ship_number):
                break
        if choice_ships == "":
            print(" Ok no worries")
            print(" Let's make it easy, there is only 1 Ship to destroy\n")
            self.ships = int(1)
            return self.ships
        print(f" You picked {choice_ships} Ships, good luck {self.name}\n")
        self.ships = int(choice_ships)
        return self.ships


class GameBoards:
    """
    class for the gameboards with methods to
    print board, place ships, get users guess and count hit ships
    """
    def __init__(self, player, board_type):
        self.board = [[" "] * (player.size) for i in range((player.size))]
        self.player = player
        self.board_type = board_type

    def print_board(self):
        """
        prints the relevent board
        technique learnt from https://www.youtube.com/watch?v=tF1WRCrd_HQ
        """
        print(f"\n {self.player.name}'s {self.board_type} \n")
        print("   ", *range(1, self.player.size + 1))
        print("   ", "+-" * self.player.size)
        row_number = 1
        for row in self.board:
            print(" ", "%d|%s|" % (row_number, "|".join(row)))
            row_number += 1

    def create_ships(self):
        """
        places relevent number of ships randomly on relevent board
        """
        for ship in range(self.player.ships):
            row, column = randint(0, (self.player.size - 1)),\
                          randint(0, (self.player.size - 1))
            while self.board[row][column] == "@":
                row, column = randint(0, (self.player.size - 1)),\
                              randint(0, (self.player.size - 1))
            self.board[row][column] = "@"
        return self.board

    def get_player_guess(self):
        """
        get input from user for row and column guess
        validate input against possible numbers
        return row and column
        """
        numbers_list = []
        for i in range(1, (self.player.size + 1)):
            numbers_list.append(str(i))
        print("\n Where would you like to Shoot? \n")
        while True:
            row = input("\n Enter the row: \n ")
            if validate_data(row, numbers_list):
                break
        while True:
            column = input("\n Enter the column: \n ")
            if validate_data(column, numbers_list):
                break
        return int(row) - 1, int(column) - 1

    def count_hit_ships(self):
        """
        count how many hits(X) are on the board
        """
        hit_boats = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    hit_boats += 1
        return hit_boats


def main():
    """
    runs the whole game
    """
    welcome()
    user = Player("", 0, 0)
    # create instance of player for the user
    Player.get_user_name(user)
    rules(user)
    game_choice = choose_game()
    Player.size_choice(user)
    Player.ships_choice(user)
    # create instances of boards for user
    user_guess_board = GameBoards(user, "Guess Board")
    user_ship_board = GameBoards(user, "Boat Board")
    # create instance of player for the computer
    comp = Player("The Enemy", user.size, user.ships)
    # create instances of boards for the computer
    comp_guess_board = GameBoards(comp, "Guess Board")
    comp_ship_board = GameBoards(comp, "Boat Board")
    GameBoards.create_ships(comp_ship_board)
    GameBoards.print_board(comp_ship_board)
    user_row, user_column = GameBoards.get_player_guess(user_guess_board)
    print(user_row, user_column)


main()
