import tkinter as tk
from tkinter import *
from tkinter import ttk

class WorldFrame(tk.Frame):
    def __init__(self,container):
        super().__init__(container)
        print("World frame initialised")
        exitButton = Button(self,text="Exit",command =self.clickExitButton)
        exitButton.pack()
        #exitButton.place(x=10,y=10)
        #self.master.config(bg="red")
        #self.background = "blue"
        #self.tk_setPalette(background="blue",bg="red")
    def clickExitButton(self):
        exit()

class CharacterFrame(tk.Frame):
    def __init__(self,container):
        super().__init__(container)
        print("Character frame initialised")
        #self.master.config(bg = "red")
        #self.config(background = "blue")
        exitButton = Button(self,text="Exit",command =self.clickExitButton)
        exitButton.pack()
    def clickExitButton(self):
        exit()

class MenuFrame(tk.Frame):
    def __init__(self,master):
        super().__init__(master) #master can be called container, nothing changes
        self.master = master #something strange is going on with master
        
        #add menus
        self.master.option_add('*tearOff', False)
        print("Menu frame initialised")
        menu=Menu(self.master)
        menu=Menu()
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        menu.add_cascade(label="Menu", menu=fileMenu)
        fileMenu.add_command(label="new",command = self.new)
        fileMenu.add_command(label="save",command = self.save)
        fileMenu.add_command(label="load",command = self.load)
        fileMenu.add_command(label="exit",command = self.exit)

        menu.add_command(label="Character",command=self.switch_to_character_frame)
        menu.add_command(label="World",command=self.switch_to_world_frame)
        #self.background = "blue"#this doesn't do anyhting :(
    
    def new(self):
        self.master.action("new")
    def save(self):
        self.master.action("save")
    def load(self):
        self.master.action("load")
    def exit(self):
        exit()

    def do_action(self,action):
        self.master.do_action(action)

    def switch_to_character_frame(self):
        self.master.switchFrame("character")
    def switch_to_world_frame(self):
        self.master.switchFrame("world")

class App(tk.Tk):
    def __init__(self,game=None):
        super().__init__()
        
        #set game
        self.game = game

        #configure the root window
        self.title("RPG")
        self.geometry("300x120")
        self.resizable(True,True)        

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
        
    def action(self,action):
        #print(action)
        self.game.do_action(action)

    def switchFrame(self,frame):
        if frame == "character":
            self.characterFrame.tkraise()
        elif frame == "world":
            self.worldFrame.tkraise()
    #def endTurn(self):
        #self.game.on_step()
        #turn_num = self.game.turn
        #self.turnLabel["text"] = str(turn_num)



if __name__ == "__main__":
    #app = App()
    #MenuFrame(app)
    #CharacterFrame(app)
    #WorldFrame(app)
    #app.mainloop()
    print("does not work (no game)")