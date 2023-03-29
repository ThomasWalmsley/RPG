import tkinter as tk
from tkinter import *
from tkinter import ttk

class LoadScreenFrame(tk.Frame):
    savegames =[]
    buttons = []
    def __init__(self,container):
        super().__init__(container)
        self.name = "Load"
        self.master = container
        self.backButton = Button(self,text="Back",command=self.master.clickBack)
        #self.savegames = self.request("get all save games")
        #if self.savegames:
            #print(self.savegames)
        self.update()

    def format_grid(self):
        gridsize = self.grid_size()
        rows = gridsize[0]
        columns = gridsize[1]
        print("rows: " + str(rows))
        print("columns: "+str(columns))
        
        for i in range(rows):
            Grid.rowconfigure(self,i,weight=1)
        for i in range(columns):
            Grid.columnconfigure(self,i,weight=1)

    def place_buttons(self):
        i=0
        for button in self.buttons:
            button.grid(row = i,column=1,sticky="nesw")
            i+=1
        gridsize = self.grid_size()
        rows = gridsize[0]
        self.backButton.grid(row=rows,column=1)

    def create_buttons(self):
        if not self.savegames:
            print("no savegames, load buttons not created")
            return
        for savegame in self.savegames:
            if savegame.endswith('.json'):
                savegame = savegame[:-5]
            print("savegame = "+savegame)
            self.buttons.append(Button(self,text=savegame,command = lambda sg = savegame:self.loadgame(sg)))

    def reset_buttons(self):
        for button in self.buttons:
            button.grid_forget()
            #destroy button eventually
            del button

    def request(self,message):
        response = self.master.request(message)
        #pass request from client to controller
        return response

    def update(self):
        self.savegames = self.request("get all save games")
        self.reset_buttons()
        self.create_buttons()
        self.place_buttons()
        self.format_grid()

    def loadgame(self,savegame):
        self.request("loadgame "+savegame)
        print("loadgame "+savegame)