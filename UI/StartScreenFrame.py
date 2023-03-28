import tkinter as tk
from tkinter import *
from tkinter import ttk

from .NewGameFrame import NewGameFrame
from.LoadScreenFrame import LoadScreenFrame

class StartScreenFrame(tk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.name = "Menu"

        self.newGameFrame = NewGameFrame(self)
        self.LoadScreenFrame = LoadScreenFrame(self)

        #self.newGameFrame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        #self.LoadScreenFrame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        #configure grid
        Grid.rowconfigure(self,0,weight=1)
        Grid.rowconfigure(self,1,weight=1)
        Grid.rowconfigure(self,2,weight=1)
        Grid.rowconfigure(self,3,weight=1)
        Grid.columnconfigure(self,2,weight=1)

        #create buttons
        #regarding continue, this button should be hidden if there are no saves stored
        continueButton = Button(self,text="Continue",command =lambda:self.buttonClick("continue"))
        newGameButton = Button(self,text="New Game",command =self.switch_to_new_game)
        LoadGameButton = Button(self,text="Load Game",command =self.switch_to_load_game)
        exitButton = Button(self,text="Exit",command =lambda:self.buttonClick("exit"))
        
        #place buttons
        continueButton.grid(row=0,column=2,sticky="nsew")
        newGameButton.grid(row=1,column=2,sticky="nsew")
        LoadGameButton.grid(row=2,column=2,sticky="nsew")
        exitButton.grid(row=3,column=2,sticky="nsew")

    def switch_to_new_game(self):
        self.newGameFrame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        self.newGameFrame.tkraise()

    def switch_to_load_game(self):
        self.LoadScreenFrame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        self.LoadScreenFrame.tkraise()
        
    def clickBack(self):
        self.newGameFrame.place_forget()
        self.LoadScreenFrame.place_forget()
        print("raise")

    def buttonClick(self,action):
        action = action
        if action == "exit":
            exit()
        if action == "continue":
            print("continue")
            #game.continue
        else:
            self.master.switchFrame(action)