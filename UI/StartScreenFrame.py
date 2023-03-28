import tkinter as tk
from tkinter import *
from tkinter import ttk

class StartScreenFrame(tk.Frame):
    def __init__(self,container):
        super().__init__(container)

        #configure grid
        Grid.rowconfigure(self,0,weight=1)
        Grid.rowconfigure(self,1,weight=1)
        Grid.rowconfigure(self,2,weight=1)
        Grid.rowconfigure(self,3,weight=1)
        Grid.columnconfigure(self,2,weight=1)

        #create buttons
        #regarding continue, this button should be hidden if there are no saves stored
        continueButton = Button(self,text="Continue",command =lambda:self.buttonClick("continue"))
        newGameButton = Button(self,text="New Game",command =lambda:self.buttonClick("newgame"))
        LoadGameButton = Button(self,text="Load Game",command =lambda:self.buttonClick("load"))
        exitButton = Button(self,text="Exit",command =lambda:self.buttonClick("exit"))
        
        #place buttons
        continueButton.grid(row=0,column=2,sticky="nsew")
        newGameButton.grid(row=1,column=2,sticky="nsew")
        LoadGameButton.grid(row=2,column=2,sticky="nsew")
        exitButton.grid(row=3,column=2,sticky="nsew")

    def buttonClick(self,action):
        action = action
        if action == "exit":
            exit()
        if action == "continue":
            print("continue")
            #game.continue
        else:
            self.master.switchFrame(action)