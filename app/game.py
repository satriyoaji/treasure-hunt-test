
import random

ROW_SIZE = 6
COLUMN_SIZE = 8

# define location
class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def toString(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def isEqualTo(self, pt):
        if (pt == None):
            return False

        if (self.x == pt.x and self.y == pt.y):
            return True

        return False

playerLocation = Point(0, 0)
treasureLocation = Point(0, 0)
obstacleLocations = []
fakeTreasureLocations = []
totalObstacleLocation = 6
totalFakeLocation = 3
isStrictMode = True

class TreasureHunt:

    def initGame(self,):
        global playerLocation
        global treasureLocation
        global totalFakeLocation
        global totalObstacleLocation
        global fakeTreasureLocations
        global obstacleLocations
        global isStrictMode

        print("\nPres 'y' to play strict mode as description on task? (strict mode player only can move to up, down, and right)")
        option = input()

        usedLocations = []

        if option == 'y':
            playerLocation = Point(4, 1)
            usedLocations = [playerLocation]
            obstacleLocations = [Point(2,2), Point(2,3), Point(2,4), Point(3,4), Point(3,6), Point(4,2)]
            for x in obstacleLocations:
                usedLocations.append(x)
        else:
            isStrictMode = False
            playerLocation = self.chooseRandomLocation(usedLocations)
            for i in range(totalObstacleLocation):
                obstacleLocations.append(self.chooseRandomLocation(usedLocations))

        treasureLocation = self.chooseRandomLocation(usedLocations)
        for i in range(totalFakeLocation):
            fakeTreasureLocations.append(self.chooseRandomLocation(usedLocations))


    def tutorial(self,):
        global isStrictMode
        print("Enjoy your game :)")
        if isStrictMode:
            print("1. press 'A' to up")
            print("2. press 'B' to right")
            print("3. press 'C' to down")
        else:
            print("1. press 'w' to up")
            print("2. press 'd' to right")
            print("3. press 's' to down")
            print("4. press 'a' to left")
        print("press 'q' for quit from game")

    # Find a point within a list and return its position, or -1 if not found

    def findPoint(self,list, pt):
        for i in range(0, len(list)):
            if (list[i].isEqualTo(pt)):
                return i
        return -1


    def drawField(self):
        global playerLocation
        global treasureLocation

        for r in range(ROW_SIZE):
            for c in range(COLUMN_SIZE):
                if COLUMN_SIZE-1 == c:
                    print("#")
                else:
                    if c == 0 or r == 0 or r == ROW_SIZE-1:
                        print("#", end=" ")
                    else:
                        if Point(r, c).isEqualTo(treasureLocation):
                            print("$", end=" ")
                        elif Point(r, c).isEqualTo(playerLocation):
                            print("X", end=" ")
                        elif self.findPoint(fakeTreasureLocations, Point(r, c)) >= 0:
                            print("$", end=" ")
                        elif self.findPoint(obstacleLocations, Point(r, c)) >= 0:
                            print("#", end=" ")
                        else:
                            print(".", end=" ")


    def chooseRandomLocation(self,used_locations):
        while True:
            location = Point(random.randint(1, ROW_SIZE-2), random.randint(1, COLUMN_SIZE-2))

            if (self.findPoint(used_locations, location) < 0):
                used_locations.append(location)
                return location


    def enterLocation(self,location):
        global playerLocation

        obstacle = self.findPoint(obstacleLocations, location)
        if obstacle >= 0:
            print("There's obstacle that cannot be crossed!")
            return True

        playerLocation = location

        print("Your current location " + playerLocation.toString())

        if treasureLocation.isEqualTo(playerLocation):
            print("Treasure was found, congratulations!")
            return False

        fakeTreasures = self.findPoint(fakeTreasureLocations, playerLocation)
        if (fakeTreasures >= 0):
            print("You found fake treasure, try again!")

        self.drawField()
        return True

    # Possible commands

    def processCommand(self,command):
        global strictMode
        if (command == "q"):
            return False

        newLocation = None

        # navigations
        if (command == "B"):
            if (playerLocation.y < COLUMN_SIZE - 2):
                newLocation = Point(playerLocation.x, playerLocation.y + 1)
        elif (command == "A"):
            if (playerLocation.x > 1):
                newLocation = Point(playerLocation.x - 1, playerLocation.y)
        elif (command == "C"):
            if (playerLocation.x < ROW_SIZE - 2):
                newLocation = Point(playerLocation.x + 1, playerLocation.y)

        if isStrictMode == False:
            if (command == "a"):
                if (playerLocation.y > 1):
                    newLocation = Point(playerLocation.x, playerLocation.y - 1)
            elif (command == "d"):
                if (playerLocation.y < COLUMN_SIZE - 2):
                    newLocation = Point(playerLocation.x, playerLocation.y + 1)
            elif (command == "w"):
                if (playerLocation.x > 1):
                    newLocation = Point(playerLocation.x - 1, playerLocation.y)
            elif (command == "s"):
                if (playerLocation.x < ROW_SIZE - 2):
                    newLocation = Point(playerLocation.x + 1, playerLocation.y)
            else:
                print("Invalid command")

        if (newLocation == None):
            print("You can't move to that direction")
            return True

        return self.enterLocation(newLocation)


    def game_loop(self):
        gameActive = self.enterLocation(playerLocation)

        while gameActive == True:
            print("\nWhat do you want to do? ")
            option = input()

            gameActive = self.processCommand(option)
