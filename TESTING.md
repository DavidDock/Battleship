## CONTENTS

* [PEP8 Linter](#pep-8)
* [General Bugs and Fixes Throughout Development](#general-bugs-and-fixes-throughout-development)
* [Manual Testing](#manual-testing)  

## PEP 8  

I used [CI Python Linter](https://pep8ci.herokuapp.com/) throughout development to make sure there were no problems and issues could be fixed along the way. I did have quite a few lines above 79 characters mainly due to long variable names but I managed to split the lines using backslashes and indentation when required.

### Final Test Results

![PEP8 Linter](assets/media/pep8_linter.PNG)  

## General Bugs and Fixes Throughout Development  

Each function caused new issues to solve which were fixed by using print statements throughout and reading error messages. These included indentation errors in game one and game two loops which were fixed through careful inspection. 
Another challenge for me came with the use of strings and integers in my different choices and validating the data given. I had to use a string for data input and lists of valid data but in some cases return integer values, this took a little time working out.

## Manual Testing  

I have tested the site using the Heroku app created and also in my local terminal throughout development.

I undertook the following manual tests:   

| Feature | Expected Outcome | Test Performed | Result | Pass/Bug fixed |  
| --- | --- | --- | --- | --- |  
| Name Input | Displays Name Entered. Displays LAZY BONES if empty string or nothing is entered. Displays error message if more than 15 characters is entered and asks to re-enter.| Stress tests with too many characters, blank space and no name. | Correct invalid message or name displayed. Although if white space infront or after input it does not look very good. | Added .strip() to improve - Fixed.
| Pick Game 1 or 2 | Displays  correct game number picked message. Displays error message if 1 or 2 is not entered and asks to re-enter. | Stress tests with letters, invalid numbers, blank space and no entry. | Correct message given if valid or invalid entry given. Allthough if blank space is infront or after a valid entry I feel it should be valid. | Added .strip() to improve - Fixed.
| Pick Battlefield Grid Size | Displays  correct size picked message if valid. Displays error message if invalid input and asks to re-enter. If nothing is entered gives random size and informs user. Creates correct size grid. | Stress tests with letters, invalid numbers, blank space and no entry. Check grid sizes when both valid choice made and random one given. | All correct messages displayed and size grid used. Allthough if blank space is infront or after a valid entry I feel it should be valid. | Added .strip() to improve - Fixed.
|  Pick Number of Ships |  Displays  correct ship amount picked message if valid. Displays error message if invalid input and asks to re-enter. If nothing is entered gives just 1 ship and informs user. Creates correct amount of ships. | Stress tests with letters, invalid numbers, blank space and no entry. Check ship number when both valid choice made and just 1 ship given. | All correct messages displayed and ships given. Allthough if blank space is infront or after a valid entry I feel it should be valid. | Added .strip() to improve - Fixed.
|