import tkinter as tk
from tkinter import *
from tkinter import ttk

from UI import *

#the App makes a window
#the App has a loop that checks for events (button clicks etc)
#the App has the UI attached to it

class App(tk.Tk):
    frames = []
    def __init__(self,controller=None):
        super().__init__()
        
        #set game
        self.contoller = controller

        #configure the root window
        self.title("RPG")
        self.geometry("300x120")
        self.resizable(True,True)   
        
        #create notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        #add frames
        self.createFrames()   
        self.placeFrames(self.frames)
        self.addFramesToNotebook(self.notebook,self.frames)


    def action(self,action):
        #print(action)
        #self.game.do_action(action)
        pass

    def switchFrame(self,frame):
        if frame == "character":
            self.characterFrame.tkraise()
        elif frame == "world":
            self.worldFrame.tkraise()
        elif frame == "newgame":
            self.newGameFrame.tkraise()
        elif frame == "load":
            self.loadScreenFrame.tkraise()
        elif frame == "continue":
            print("continue")
            
    def createFrames(self):
        characterFrame=CharacterFrame(self)
        worldFrame=WorldFrame(self)
        #newGameFrame=NewGameFrame(self)
        startScreenFrame=StartScreenFrame(self)
        #loadScreenFrame=LoadScreenFrame(self)

        self.frames.append(startScreenFrame)
        self.frames.append(characterFrame)
        self.frames.append(worldFrame)
        #self.frames.append(newGameFrame)
        #self.frames.append(loadScreenFrame)
        
    def placeFrames(self,frames):
        for frame in frames:
            frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

    def addFramesToNotebook(self,notebook,frames):
        for frame in frames:
            notebook.add(frame,text=frame.name)
            



if __name__ == "__main__":
    print("does not work (no game)")