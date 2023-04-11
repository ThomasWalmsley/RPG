import tkinter as tk
from tkinter import *
from tkinter import ttk

from request import Request
from requestType import RequestType

class LoadScreenFrame(tk.Frame):
    savegames =[]
    buttons = []
    def __init__(self,container):
        super().__init__(container)
        self.name = "Load"
        self.master = container
        self.update()

    def format_grid(self):
        gridsize = self.grid_size()
        rows = gridsize[0]
        columns = gridsize[1]      
        for i in range(rows):
            Grid.rowconfigure(self,i,weight=1)
        Grid.columnconfigure(self,1,weight=1)

    def place_buttons(self):
        i=0
        for button in self.buttons:
            button.grid(row = i,column=1,sticky="nesw")
            i+=1
        gridsize = self.grid_size()
        rows = gridsize[0]
        self.backButton.grid(row=len(self.buttons)+1,column=1)

    def create_buttons(self):
        self.backButton = Button(self,text="Back",command=self.master.clickBack)
        if not self.savegames:
            print("no savegames, load buttons not created")
            return
        for savegame in self.savegames:
            if savegame.endswith('.json'):
                savegame = savegame[:-5]
            self.buttons.append(Button(self,text=savegame,command = lambda sg = savegame:self.loadgame(sg)))


    def clear(self):
        list = self.grid_slaves()
        for l in list:
            l.destroy()

    def send_request(self,request):  
        response = self.master.send_request(request)
        #pass request from client to controller
        return response

    def update(self):
        #request all savegames
        #request = Request(RequestType.load,"help!")
        #self.send_request(request)
        self.savegames = self.send_request("get all save games")
        self.clear()
        self.buttons = []
        self.create_buttons()
        self.place_buttons()
        self.format_grid()

    def loadgame(self,savegame):
        print("savegame = "+savegame)
        request = Request(RequestType.load,savegame)
        self.send_request(request)
        #self.send_request("loadgame "+savegame)