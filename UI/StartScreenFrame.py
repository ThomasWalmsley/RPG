import tkinter as tk
from tkinter import *
from tkinter import ttk

from .NewGameFrame import NewGameFrame
from.LoadScreenFrame import LoadScreenFrame
from request import Request
from response import Response
from requestType import RequestType

class StartScreenFrame(tk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.name = "Menu"
        self.master=container
        self.newGameFrame = NewGameFrame(self)
        self.LoadScreenFrame = LoadScreenFrame(self)
        #print(self.master.request("state"))
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
        self.saveButton = Button(self,text="save",command = lambda:self.buttonClick("save"))
        self.continueButton = Button(self,text="Continue",command =lambda:self.buttonClick("continue"))
        newGameButton = Button(self,text="New Game",command =self.switch_to_new_game)
        LoadGameButton = Button(self,text="Load Game",command =self.switch_to_load_game)
        exitButton = Button(self,text="Exit",command =lambda:self.buttonClick("exit"))
        
        #place buttons

        self.update()
        #continueButton.grid(row=0,column=2,sticky="nsew")
        #self.saveButton.grid(row=0,column=2,sticky="nsew")
        
        newGameButton.grid(row=1,column=2,sticky="nsew")
        LoadGameButton.grid(row=2,column=2,sticky="nsew")
        exitButton.grid(row=3,column=2,sticky="nsew")

    def update(self):
        #get controller state
        controllerstate= self.send_request("state")
        latestSave = self.send_request("latestsave")
        if controllerstate =="start" and latestSave:
            self.continueButton.grid(row=0,column=2,sticky="nsew")
            self.saveButton.grid_forget()
        elif controllerstate =="started":
            self.continueButton.grid_forget()
            self.saveButton.grid(row=0,column=2,sticky="nsew")
        #else:

    def switch_to_new_game(self):
        self.newGameFrame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        self.newGameFrame.tkraise()

    def switch_to_load_game(self):
        self.LoadScreenFrame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        self.LoadScreenFrame.tkraise()
        self.LoadScreenFrame.update()
        
    def clickBack(self):
        self.newGameFrame.place_forget()
        self.LoadScreenFrame.place_forget()
        #print("raise")

    def buttonClick(self,action):
        action = action
        if action == "exit":
            exit()
        if action == "continue":
            self.master.request("changestate started")
            savegame = self.send_request("latestsave")
            self.send_request("loadgame "+savegame)   
            #self.request(Request())
            self.update()
        elif action == "save":
            self.master.request("save")
            request = Request(RequestType.save,"game")
            self.send_request(Request())
        else:
            print("Functionality not implemented")

    def send_request(self,request):
        #response = self.master.request(message)
        #pass request from client to controller
        #self.master.request(request)
        response = self.master.send_request(request)
        return response