from tkinter import *
from game import Game
from app import App

#create game class
game = Game()

#ui
app = App(game)
app.mainloop()
