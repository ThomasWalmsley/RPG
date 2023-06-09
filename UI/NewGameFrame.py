import tkinter as tk
from tkinter import *
from tkinter import ttk

class NewGameFrame(tk.Frame):
    #enter name of new world
        #text box
    #world options
        #tech level
        #difficulty
        #population

    #save game
    #kill old game
    #create new game

    def __init__(self,container):
        super().__init__(container)
        self.name = "New"
        self.master = container

        #grid configure
        Grid.rowconfigure(self,1,weight =1)
        Grid.rowconfigure(self,2,weight =1)
        Grid.rowconfigure(self,3,weight =1)
        Grid.columnconfigure(self,1,weight =1)

        # TextBox Creation
        self.inputtxt = tk.Text(self,
            height = 5,
            width = 10)
        #self.inputtxt.pack()
        self.inputtxt.grid(column=1, row=1,sticky = "nesw")
        
        #Button Create New World
        createNewWorldButton = Button(self,text="Create",command = self.create_new_world)
        createNewWorldButton.grid(column=1, row=2,)

        #Button Back
        backButton = Button(self,text="Back",command = self.master.clickBack)
        backButton.grid(column=1, row=3,)

    def retrieve_input(self):
        input = self.inputtxt.get("1.0",'end-1c')
        return input

    def create_new_world(self):
        name =   self.retrieve_input()
        self.send_request("create world "+name)

    def send_request(self,message):
        self.master.send_request(message)