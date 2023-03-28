import tkinter as tk
from tkinter import *
from tkinter import ttk

class LoadScreenFrame(tk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.name = "Load"
        self.master = container
        backButton = Button(self,text="Back",command=self.master.clickBack)
        backButton.grid(row=1,column=1)