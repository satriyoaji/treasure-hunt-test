from app.game import Point
from app.game import TreasureHunt

load = Point(0, 0)
game = TreasureHunt()
game.initGame()
game.tutorial()
game.game_loop()
print("Thanks for playing!")
