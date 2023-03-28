from tkinter import *
from game import Game
from app import App
from controller import Controller

#create controller
controller = Controller()

#create game class
#game = Game(controller)

#ui
app = App(controller)
app.mainloop()
