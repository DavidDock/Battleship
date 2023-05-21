# Battleship!  
This is a computerised variation of the classic board game Battleship.  
You attempt to win the war by sinking all the enemy's ships, More information about the history of the game can be found here on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)).  
This version of the game lets you choose battlefield grid size, amount of ships and provides you the choice of two game types.

Visit the deployed site: [Battleship](https://battleship-ddocksey.herokuapp.com/)

## CONTENTS

* [Planning](#planning)
  * [User Stories](#user-stories)
  * [Design](#design)
  * [Flowcharts](#flowcharts)

* [Features](#features)
  * [Name Input and Rules](#name-input-and-rules)
  * [Game Choices](#game-choices)
  * [Start of Game](#start-of-game)
  * [Game One](#game-one)
  * [Game Two](#game-two)
  * [Play Again?](#play-again)
  * [Validate Inputs](#validate-inputs)
  * [Languages Used](#languages-used)
  * [Future Implementations](#future-implementations)
  * [Data Model](#data-model)

* [Deployment](#deployment)
* [Testing](#testing)
* [Credits](#credits)


## Planning

### User Stories  
#### User goals
* As a user I want to clearly know what I am doing.
* As a user I want to play a game against a computer to see if I come out on top. 
* As a returning user I would like to play again and show my friends.

#### The websites goals
* As the site owner I want to entertain the user.
* As the site owner I would like to provide a game that is easy to understand.
* As the site owner I would like all user inputs to provide feedback and let the game continue.
* As the site owner I would like to encourage the user to play more than once and return to the site.

#### How will the goals be acheived  
* Instructions on how to play the game will be provided to make it easy to understand.
* Added options of picking battlefield grid size, ships and game type will provided added entertainment and encourage the user to return.
* On every input there will be a loop until valid input is given, with feedback given if invalid input is entered.

### Flowcharts  

I created three flowcharts. One  to show the running of the whole game and one each for the different game types:

![Flowchart for the whole game](assets/media/battleship_flowchart.jpeg)  

![Flowchart for game type one](assets/media/game_type_one.jpeg)  

![Flowchart for game type two](assets/media/game_type_two.jpeg)  

## Design  
This game is based inside a mock terminal deployed via Heroku and has basic design. I have added a welcome image using ASCII art.

## Features  

### Name Input and Rules

### Game Choices

### Start of Game

### Game One 

### Game Two

### Play Again

### Validate Inputs

### Languages Used  
Python

### Future Implementations  
* Add the option for the user to place their ships.
* Add a variation of ship sizes.
* Create a multiplayer game where two humans take turns.

## Data Model  
I chose to create three classes for this game:  

1. Player Class
* This creates instances for the players. With attributes of name, size of battlefield grid and amount of ships.
* The methods in this class names the player, allows the player to choose battlefield grid size and amount of ships.
* In this game a user instance and a computer instance are created for each time you play. The user is created once you enter your name.  

2. GameBoards Class:
* This creates instances for each board required. With attributes of the player (created in the Player class) and board type.
* The methods in this class are printing one or two boards, creating ships on the board, getting the players shot coordinates and counting remaining ships on the board.
* In this game four boards are created. A ship board and a guess board for both the user and computer.

3. GameType class:
* This creates an instance for each type of game. With attributes of amount of turns, each player created and each board created.
* The methods in this class are game type one and game type two, running the relevant game chosen by the user.

## Deployment  
The steps to deploy using [Heroku](https://id.heroku.com/login): 
* Select new in the top right corner of the dashboard and create new app on dropdown menu.
* Name the app and choose region and select create app.
* In the created app's settings click reveal Config Vars and set value to PORT and KEY to 8000 and select add.
* This app did not require any other Config Variables to add.
* Below Config Vars select Add Buildpack and select Python and then Node.js making sure the two are in that order.
* Go to deploy section and choose github as deployment method, this will connect to github then connect the correct repository.
* Then you can either select Automatic deploy or deploy manually and click deploy branch.
* The app will then be deployed.
* This game had no additional dependincies that needed to be added to the requirements.txt file but if it did you'd need to type into the terminal pip3 freeze requirements.txt to update it.

To Fork the repository:  
* In Github go to the repository [https://github.com/DavidDock/Battleship](https://github.com/DavidDock/Battleship).
* Click the fork button in the top right corner.  

To Clone the repository:  
* In Github go to the repository [https://github.com/DavidDock/Battleship](https://github.com/DavidDock/Battleship).
*  Click the Code button and select if you'd like to clone with HTTPS, SSH or Github CLI and copy the link underneath.
* Open your terminal in your code editor and change the working directory to the location you want to use for the cloned directory.
* Type 'git clone', paste the link you copied and press enter.
* If using the code institute template there will be no need to set up the virtual environment.
## Testing
Please refer to [TESTING.MD](TESTING.md)  

## Credits
### Learning  
The code used for this project was taught to me by code insitute. Code Insitutes project run through 'love sandwiches' helped me greatly with the concepts needed in my project including deploying the site with Heroku and creating a seperate function to validate data. Code insitutes scope video for battleship also helped me understand the concept of building the game and the use of classes.

### New learning

To gain a greater understanding I also watched Knowledge Mavens Battleship tutorial videos, [How to Code Battleship in Python](https://www.youtube.com/watch?v=tF1WRCrd_HQ) and [Python Battleship with Object Oriented Programming](https://www.youtube.com/watch?v=alJH_c9t4zw). I found it really helped me understand each function required. It particularly helped with the method I used to print the board, further learnt on [Stackoverflow](https://stackoverflow.com/questions/4288973/whats-the-difference-between-s-and-d-in-python-string-formatting).
I also found [Stackoverflow](https://stackoverflow.com/questions/23623288/print-full-ascii-art) useful for creating my welcome message.  
As per my mentors advice I learnt about best practices on writing Docstrings from [https://www.geeksforgeeks.org/python-docstrings/](https://www.geeksforgeeks.org/python-docstrings/) and implemented this learning into my Docstring writing.

## Content and Media  

* My flowcharts were made using [lucid](https://lucid.app/).