from human import Human
from gui import Gui

jack = Human('Jack', 26)

game = Gui(jack)

game.run_game()