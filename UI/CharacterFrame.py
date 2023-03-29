import tkinter as tk
from tkinter import *
from tkinter import ttk

class CharacterFrame(tk.Frame):
    def __init__(self,container):
        super().__init__(container)
        #print("Character frame initialised")
        self.name = "Character"
        #self.master.config(bg = "red")
        #self.config(background = "blue")
        #characterPortraitButton = Button(self,text="Face",command =None,padx=20,pady=10)

        #configure grid
        Grid.rowconfigure(self,1,weight=1)    
        Grid.rowconfigure(self,2,weight=1)
        Grid.rowconfigure(self,3,weight=1)
        Grid.rowconfigure(self,4,weight=1)
        Grid.rowconfigure(self,5,weight=1)
        Grid.rowconfigure(self,6,weight=1) 
        Grid.rowconfigure(self,7,weight=1) 
        Grid.rowconfigure(self,8,weight=1) 
        
        Grid.columnconfigure(self,1,weight=1)
        Grid.columnconfigure(self,2,weight=1)

        #create widgets
        characterPortraitButton = Button(self,text="Face",command =None)
        funnyLabel = Label(self,text="Character")
        characternameLabel = Label(self,text ="Name")
        ageLabel = Label(self,text="Age")
        actionPointsLabel = Label(self,text="Action Points")
        statsLabel = Label(self,text="stats")
        raceLabel = Label(self,text="race")
        religionLabel = Label(self,text="religion")
        

        #place widgets
        #column 1
        characterPortraitButton.grid(row=1,column = 1, rowspan=2, sticky="nesw")
        characternameLabel.grid(row=3,column = 1, rowspan=1, sticky="nesw")
        ageLabel.grid(row=4,column = 1, rowspan=1, sticky="nesw")
        actionPointsLabel.grid(row=5,column = 1, rowspan=1, sticky="nesw")
        statsLabel.grid(row=6,column = 1, rowspan=1, sticky="nesw")
        raceLabel.grid(row=7,column = 1, rowspan=1, sticky="nesw")
        religionLabel.grid(row=8,column = 1, rowspan=1, sticky="nesw")
        
        #column 2
        funnyLabel.grid(row=1,column=2,rowspan=6,sticky="nesw")