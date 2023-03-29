from tkinter import *
from game import Game
from app import App
from controller import Controller

#create controller
controller = Controller()
controller.check_saves_folder()
#create game class
#game = Game(controller)
#game.save_game()
controller.save_game()
controller.save_options()
controller.load_options()
#ui
app = App(controller)
app.mainloop()

