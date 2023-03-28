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

        self.createFrames()   

        #Menu Frame
        menuFrame = MenuFrame(self)
        
        #Character Frame
        self.characterFrame = CharacterFrame(self)
        self.characterFrame["bg"]="red"
        self.characterFrame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        
        #World Frame
        self.worldFrame = WorldFrame(self)
        self.worldFrame["bg"]="blue"
        self.worldFrame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        
        #new game Frame
        self.newGameFrame = NewGameFrame(self)
        self.newGameFrame["bg"]="green"
        self.newGameFrame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        
        #Start Screen Frame
        self.startScreenFrame = StartScreenFrame(self)
        self.startScreenFrame["bg"]="purple"
        self.startScreenFrame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        
        #Load Screen Frame
        self.loadScreenFrame = LoadScreenFrame(self)
        self.loadScreenFrame["bg"]="orange"
        self.loadScreenFrame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        self.loadScreenFrame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        #bring start screen to front
        self.startScreenFrame.tkraise()
        #self.frames[]

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

        menuFrame=MenuFrame(self)
        characterFrame=CharacterFrame(self)
        worldFrame=WorldFrame(self)
        newGameFrame=NewGameFrame(self)
        startScreenFrame=StartScreenFrame(self)
        loadScreenFrame=LoadScreenFrame(self)

        self.frames.append(menuFrame)
        self.frames.append(characterFrame)
        self.frames.append(worldFrame)
        self.frames.append(newGameFrame)
        self.frames.append(startScreenFrame)
        self.frames.append(loadScreenFrame)
        

    def placeFrames(self,frames):
        for frame in frames:
            frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)



if __name__ == "__main__":
    #app = App()
    #MenuFrame(app)
    #CharacterFrame(app)
    #WorldFrame(app)
    #app.mainloop()
    print("does not work (no game)")