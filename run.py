from tkinter import *
from game import Game
from app import App
from controller import Controller

#create controller
controller = Controller()

#ui
app = App(controller)
app.mainloop()

