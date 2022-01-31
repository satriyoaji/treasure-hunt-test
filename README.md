### 2. Running Treasure Hunt App ###
* Make sure your machine is already installed python 3.7, before running PoC application.
* Treasure Hunt App no need any library to run, only python 3.7.
* First, run app:
    ```bash
    python .\index.py
    ```
* You will see some option to pick on app :
    ```bash
    1 : Print Map
    2 : Print Map with treasure
    3 : Print Treasure Position
    4 : Re-position of Treasure
    9 : Play Time!
    0 : Exit
    Option : <choice>
    ```
  Choice :
    ```bash
    1. to print Treasure Map
    2. to print Treasure Map (with treasure marking)
    3. to print Treasure Coordinate
    4. randomize treasure position and set how much treasure appear on the map
    9. play the game
    0. exit from loop
    ```
* When you pick choice 9 for playing treasure hunt, app will show :
    ```bash
    >> Map <<
    ######## 
    #......# 
    #.###..# 
    #...#.##
    #X#....#
    ########
    >> Map With Treasure <<
    ########
    #....$.#
    #.###..#
    #...#.##
    #X#....#
    ########
    Treasure position : [[1, 5]]
    ```
* The map and input movement are following Assessment Instruction, so you only can move up, right and down.