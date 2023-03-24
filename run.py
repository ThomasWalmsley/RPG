from tkinter import *
from ui import Window
from game import Game
#create game class
game = Game()

#drawWindow()
root = Tk()
app = Window(root,game)
root.wm_title("Tkinter window")
root.geometry("320x200")
root.mainloop()