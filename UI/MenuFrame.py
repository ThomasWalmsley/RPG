import tkinter as tk
from tkinter import *
from tkinter import ttk

class MenuFrame(tk.Frame):
    def __init__(self,master):
        super().__init__(master) #master can be called container, nothing changes
        self.master = master #something strange is going on with master
        
        #add menus
        self.master.option_add('*tearOff', False)
        #print("Menu frame initialised")
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
        self.master.switchFrame("newgame")
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