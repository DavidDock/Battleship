# import random number
from random import randint


def welcome():
    """
    Prints welcome message to player.

    Learnt from:
    https://stackoverflow.com/questions/23623288/print-full-ascii-art
    """
    print(r"""
         =======         _
        //     ||      _//
       //      ||     |  |
  ==========================
  \\      WELCOME TO      //
   \\     BATTLESHIP     //
    ======================
            """)


def rules(user):
    """
    Describes rules for each game type.

    Parameters:
    user: user is an instance created in Player class
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
    Function to validate player input.

    Inspired by codes institutes love sandwiches walkthrough.

    Parameters:
    data(str): data  that needs to be checked if valid
    data_list(list): a list of valid data

    Returns:
    True or false(bool): Returns true if data is valid and false if invalid
    """
    try:
        if data not in data_list:
            raise ValueError(
                f"Please choose : {' '.join(data_list)}")
    except ValueError as e:
        print(f" Invalid entry. {e} \n")
        return False
    return True


def choose_game():
    """
    Get player to choose game type and validate input.

    Returns:
    game_pick(str): The choice of game type
    """
    game_choices = ["1", "2"]
    while True:
        game_pick = input(" Pick your Game: 1 or 2? \n ").strip()
        if validate_data(game_pick, game_choices):
            break
    print(f"\n You picked Game {game_pick} \n")
    return game_pick


def end_game():
    """
    Function for end of game.

    Asks player if they want to play again and validates input.
    Either plays the game again or says goodbye depending on input.
    """
    end_choices = ["Y", "N"]
    while True:
        end_choice = input(" Play again?: Y or N \n ").strip().upper()
        if validate_data(end_choice, end_choices):
            break
    if end_choice == "Y":
        main()
    else:
        print("\n Thanks for playing")


class Player:
    """
    Class for player with methods to
    get name, grid size and  number of ships.

    Attributes:
        name(str): The Players name.
        size(int): The size of battlefield grid.
        ships(int): The amount of ships in game.
    """

    def __init__(self, name, size, ships):
        """
        The constructor for Player class.

        Parameters:
            name(str): The Players name.
            size(int): The size of battlefield grid.
            ships(int): The amount of ships in game.
        """
        self.name = name
        self.size = size
        self.ships = ships

    def get_user_name(self):
        """
        Gets user input for their name and names Player.

        Makes sure name is not too long and
        if name is blank, it gives user a name.

        Parameters:
            self: Player instance.

        Returns:
            name(str): New name for Player.
        """
        user_name = input(" Ok Captain what is your name? \n ").strip().upper()
        while len(user_name) > 15:
            print("\n Please choose a name with a max of 15 characters \n")
            user_name = input().strip().upper
        if user_name == "":
            user_name = "LAZY BONES"
        self.name = user_name
        return self.name

    def size_choice(self):
        """
        Gets user input for grid size, validates and updates Players size.

        Parameters:
            self: Player instance.

        Returns:
            size(int): New size for Player.
        """
        grids = ["4", "5", "6", "7", "8", ""]
        while True:
            print("\n Pick your battlefield grid size:\n")
            choice = input(" 4 5 6 7 or 8? \n ").strip()
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
        Gets user input for ship amount, validates and updates Players ships.

        Parameters:
            self: Player instance.

        Returns:
            ships(int): New ships for Player.
        """
        ship_number = ["1", "2", "3", "4", "5", "6", "7", "8", ""]
        while True:
            print(" Pick the number of Ships: ")
            choice_ships = input(" 1 2 3 4 5 6 or 8? \n ").strip()
            if validate_data(choice_ships, ship_number):
                break
        if choice_ships == "":
            print(" Ok no worries")
            print(" Let's make it easy, there is only 1 Ship to destroy\n")
            self.ships = int(1)
            return self.ships
        print(f"\n You picked {choice_ships} Ships, good luck {self.name}\n")
        self.ships = int(choice_ships)
        return self.ships


class GameBoards:
    """
    Class for the gameboards with methods to
    print board, place ships, get users guess and count remaining ships.

    Attributes:
        board(list): A list of empty lists the size of the players size choice.
        player: The player created in Player class.
        board_type(str): The type of board, either guess board or ship board.
    """

    def __init__(self, player, board_type):
        """
        The constructor for GameBoards class.

        Parameters:
            board(list): A list of empty lists the size of players size choice.
            player: The player created in Player class.
            board_type(str): Type of board, either guess board or ship board.
        """
        self.board = [[" "] * (player.size) for i in range((player.size))]
        self.player = player
        self.board_type = board_type

    def print_board(self):
        """
        Prints the relevent board.

        technique learnt from https://www.youtube.com/watch?v=tF1WRCrd_HQ

        Parameters:
            self: GameBoards instance.
        """
        print(f"\n {self.player.name}'s {self.board_type} \n")
        print("   ", *range(1, self.player.size + 1))
        print("   ", "+-" * self.player.size)
        row_number = 1
        for row in self.board:
            print(" ", "%d|%s|" % (row_number, "|".join(row)))
            row_number += 1

    def print_two_boards(self, board_two):
        """
        Prints two boards next to each other.

        Parameters:
            self: GameBoards instance.
            board_two: Second required Gameboards instance.
        """
        print(f" {self.player.name} here are your boards: ")
        print(f"\n {self.board_type}"
              f"{' ' * (self.player.size * 2)}"
              f" {board_two.board_type}  \n")
        print("  ", *range(1, self.player.size + 1), " " * 11,
              *range(1, self.player.size + 1))
        print("  ", "+-" * self.player.size, " " * 10,
              "+-" * self.player.size)
        row_number = 1
        for row1, row2 in zip(self.board,
                              board_two.board):
            print("", "%d|%s|" % (row_number, "|".join(row1)),
                  " " * 8, "%d|%s|" % (row_number, "|".join(row2)))
            row_number += 1

    def create_ships(self):
        """
        Places relevent number of Player ships randomly on Player board.

        Parameters:
            self: GameBoards instance.

        Returns:
            self.board(list): New board marked with ships.
        """
        for _ in range(self.player.ships):
            row, column = randint(0, (self.player.size - 1)),\
                randint(0, (self.player.size - 1))
            while self.board[row][column] == "@":
                row, column = randint(0, (self.player.size - 1)),\
                    randint(0, (self.player.size - 1))
            self.board[row][column] = "@"
        return self.board

    def get_player_guess(self):
        """
        Gets input from user for row and column guess and validates data.

        Parameters:
            self: GameBoards instance.

        Returns:
            row(int), column(int): Users guess for row and column.
        """
        numbers_list = []
        for i in range(1, (self.player.size + 1)):
            numbers_list.append(str(i))
        print("\n Where would you like to Shoot? ")
        while True:
            row = input("\n Enter the row: \n ").strip()
            if validate_data(row, numbers_list):
                break
        while True:
            column = input("\n Enter the column: \n ").strip()
            if validate_data(column, numbers_list):
                break
        return int(row) - 1, int(column) - 1

    def count_rem_ships(self):
        """
        Counts how many remaining ships(@) are on the board.

        Parameters:
            self: GameBoards instance.

        Returns:
            remaining_ships(1): Ships(@) left on the board.
        """
        remaining_ships = 0
        for row in self.board:
            for column in row:
                if column == "@":
                    remaining_ships += 1
        return remaining_ships


class GameType:
    """
    Class for the GameType with methods to playe type one or two.

    Attributes:
        turns(int): Number of shots in the game.
        player_one: The player created in Player class.
        player_two: Player two created in Player class.
        player_one_ship_board:
            Player ones ship board created in GameBoards Class.
        player_one_guess_board:
            Player ones guess board created in GameBoards Class.
        player_two_ship_board:
            Player twos ship board created in GameBoards Class.
        player_two_guess_board:
            Player twos guess board created in GameBoards Class.
    """

    def __init__(self, turns, player_one, player_two, player_one_ship_board,
                 player_one_guess_board, player_two_ship_board,
                 player_two_guess_board):
        """
        The constructor for GameType class.

        Parameters:
        turns(int): Number of shots in the game.
        player_one: The player created in Player class.
        player_two: Player two created in Player class.
        player_one_ship_board:
            Player ones ship board created in GameBoards Class.
        player_one_guess_board:
            Player ones guess board created in GameBoards Class.
        player_two_ship_board:
            Player twos ship board created in GameBoards Class.
        player_two_guess_board:
            Player twos guess board created in GameBoards Class.
        """
        self.turns = turns
        self.player_one = player_one
        self.player_two = player_two
        self.player_one_ship_board = player_one_ship_board
        self.player_one_guess_board = player_one_guess_board
        self.player_two_ship_board = player_two_ship_board
        self.player_two_guess_board = player_two_guess_board

    def play_game_one(self):
        """
        Runs game type one.

        Parameters:
            self: GameType instance.
        """
        # print Key for board
        print(" KEY: \n"
              " X = Hit ship \n"
              " - = Missed shot ")
        GameBoards.create_ships(self.player_two_ship_board)
        # while loop for when still turns left
        while True:
            GameBoards.print_board(self.player_one_guess_board)
            user_row, user_column = GameBoards.get_player_guess(
                self.player_one_guess_board)
            # check if input is guessed aleady
            while self.player_one_guess_board.board[user_row][user_column] \
                    == "-" or \
                    self.player_one_guess_board.board[user_row][user_column] \
                    == "X":
                print(" Those coordinates have been guessed already \n")
                user_row, user_column \
                    = GameBoards.get_player_guess(self.player_one_guess_board)
            # check if player hit or missed a ship
            if self.player_two_ship_board.board[user_row][user_column] == "@":
                print(f" {self.player_one.name} sunk a ship! \n")
                self.player_one_guess_board.board[user_row][user_column] = "X"
                self.player_two_ship_board.board[user_row][user_column] = "X"
            else:
                print(f" {self.player_one.name} missed! \n")
                self.player_one_guess_board.board[user_row][user_column] = "-"
                self.player_two_ship_board.board[user_row][user_column] = "-"
            # check if player has hit all ships
            if GameBoards.count_rem_ships(self.player_two_ship_board) == 0:
                print(f" {self.player_one.name} hit all the ships!"
                      " Congratulations, the war is won! \n")
                GameBoards.print_board(self.player_two_ship_board)
                print("\n")
                break
            # check if player has enough shots left to win
            elif self.turns - 1 < \
                    GameBoards.count_rem_ships(self.player_two_ship_board):
                print(f" Sorry {self.player_one.name}, you loose the war! \n"
                      " You've not enough shots left to sink all the ships \n")
                GameBoards.print_board(self.player_two_ship_board)
                print("\n")
                break
            else:
                self.turns -= 1
                print(f" You have {self.turns} turns remaining ")

    def play_game_two(self):
        """
        Runs game type two.

        Parameters:
            self: GameType instance.
        """
        # print Key for board
        print(" KEY: \n"
              " @ = Ship \n"
              " X = Hit ship \n"
              " - = Missed shot \n")
        # create ships for both players
        GameBoards.create_ships(self.player_one_ship_board)
        GameBoards.create_ships(self.player_two_ship_board)
        # loop for whole game until end
        while True:
            # loop for each round of player one turn
            while True:
                # print relevent boards
                GameBoards.print_two_boards(self.player_one_guess_board,
                                            self.player_one_ship_board)
                # get player ones guess and check if its already been guessed
                p1_row, p1_column \
                    = GameBoards.get_player_guess(self.player_one_guess_board)
                if self.player_one_guess_board.board[p1_row][p1_column] \
                    == "-" or \
                    self.player_one_guess_board.board[p1_row][p1_column] \
                        == "X":
                    print(" Those coordinates have been guessed already \n")
                # check if shot hit a ship and update boards
                elif self.player_two_ship_board.board[p1_row][p1_column] \
                        == "@":
                    print(f" {self.player_one.name} sunk a ship! \n")
                    self.player_one_guess_board.board[p1_row][p1_column] = "X"
                    self.player_two_ship_board.board[p1_row][p1_column] = "X"
                    break
                else:
                    # update miss on boards
                    print(f"\n {self.player_one.name} missed a shot \n")
                    self.player_one_guess_board.board[p1_row][p1_column] = "-"
                    self.player_two_ship_board.board[p1_row][p1_column] = "-"
                    break
            # check if all player twos ships have been sunk
            if GameBoards.count_rem_ships(self.player_two_ship_board) == 0:
                print(f" {self.player_one.name} hit all the ships!"
                      " Congratulations, the war is won! \n")
                GameBoards.print_board(self.player_two_ship_board)
                print("\n")
                break
            # loop for player two turn
            while True:
                # get random guess
                p2_row, p2_column \
                    = randint(0, (self.player_two.size - 1)), \
                    randint(0, (self.player_two.size - 1))
                # loop until guess is not guessed before
                while self.player_two_guess_board.board[p2_row][p2_column] \
                    == "-" or \
                        self.player_two_guess_board.board[p2_row][p2_column] \
                        == "X":
                    p2_row, p2_column \
                        = randint(0, (self.player_two.size - 1)), \
                        randint(0, (self.player_two.size - 1))
                # check if player two hit and update boards
                if self.player_one_ship_board.board[p2_row][p2_column] == "@":
                    self.player_two_guess_board.board[p2_row][p2_column] = "X"
                    self.player_one_ship_board.board[p2_row][p2_column] = "X"
                    print(f" {self.player_two.name} sunk a ship \n")
                    break
                # update missed shot on boards
                else:
                    print(f" {self.player_two.name} missed a shot \n")
                    self.player_two_guess_board.board[p2_row][p2_column] = '-'
                    self.player_one_ship_board.board[p2_row][p2_column] = '-'
                    break
            # check if player two has sunk all ships
            if GameBoards.count_rem_ships(self.player_one_ship_board) == 0:
                print(f" Sorry {self.player_one.name}, the war is lost \n")
                GameBoards.print_board(self.player_one_ship_board)
                break


def main():
    """
    Runs the whole game.

    Creates relevant instances and calls all functions needed.
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
    user_ship_board = GameBoards(user, "Ship Board")
    # create instance of player for the computer
    comp = Player("The Enemy", user.size, user.ships)
    # create instances of boards for the computer
    comp_guess_board = GameBoards(comp, "Guess Board")
    comp_ship_board = GameBoards(comp, "Ship Board")
    turns = 12
    # create intance of game type
    game = GameType(turns, user, comp, user_ship_board, user_guess_board,
                    comp_ship_board, comp_guess_board)
    # runs game 1 or 2 depending on choice
    if game_choice == "1":
        GameType.play_game_one(game)
    else:
        GameType.play_game_two(game)
    # runs end game function to see if they want to play again
    end_game()


main()
