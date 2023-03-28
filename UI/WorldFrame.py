import tkinter as tk
from tkinter import *
from tkinter import ttk

class WorldFrame(tk.Frame):
    def __init__(self,container):
        super().__init__(container)
        print("World frame initialised")

        notebook = ttk.Notebook(self)

        notebook.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        frame1 = Frame(notebook,bg="blue")
        frame2 = Frame(notebook,bg="red")

        frame3 =AreaFrame(notebook)
        frame4 =TownFrame(notebook)
        frame5 = ShopFrame(notebook)

        frame3.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        frame4.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        frame5.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        notebook.add(frame3,text="Area")
        notebook.add(frame4,text="Town")
        notebook.add(frame5,text="Shop")

class AreaFrame(tk.Frame):
    def __init__(self,container):
        super().__init__(container)
        print("Area frame initialised")

        #Location Label
        location = "area"
        locationLabel =Label(self,text="You are in " + location)

        #place widgets
        locationLabel.grid(row=1,column=1,columnspan = 4)

class TownFrame(tk.Frame):
    def __init__(self,container):
        super().__init__(container)
        print("Town frame initialised")

class ShopFrame(tk.Frame):
    def __init__(self,container):
        super().__init__(container)
        print("Shop frame initialised")