import tkinter as tk
from tkinter import *
from tkinter import ttk

class WorldFrame(tk.Frame):
    def __init__(self,container):
        super().__init__(container)
        #print("World frame initialised")
        self.name = "World"
        notebook = ttk.Notebook(self)

        notebook.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        frame1 = Frame(notebook,bg="blue")
        frame2 = Frame(notebook,bg="red")

        frame3 =AreaFrame(notebook)
        frame4 =TownFrame(notebook)
        frame5 = ShopFrame(notebook)

        frame3.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        frame4.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        frame5.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        notebook.add(frame3,text="Area")
        notebook.add(frame4,text="Town")
        notebook.add(frame5,text="Shop")

class AreaFrame(tk.Frame):
    def __init__(self,container):
        super().__init__(container)
        #print("Area frame initialised")

        #configure grid
        Grid.rowconfigure(self,1,weight=1)
        Grid.rowconfigure(self,2,weight=1)
        Grid.rowconfigure(self,3,weight=1)
        Grid.rowconfigure(self,4,weight=1)
        Grid.rowconfigure(self,5,weight=1)
        Grid.rowconfigure(self,6,weight=1)
        Grid.columnconfigure(self,1,weight=1)
        Grid.columnconfigure(self,2,weight=1)
        Grid.columnconfigure(self,3,weight=1)

        

        #Location Label
        location = "area"
        locationLabel =Label(self,text="You are in " + location)
        
        #Headers
        factionsLabel = Label(self,text="Factions",bg="grey")
        townsLabel = Label(self,text="Towns",bg="grey")
        otherLabel = Label(self,text="other_idk",bg="grey")
        
        #data (towns, factions etc)
        town1Label = Button(self,text="Town1")
        town2Label = Button(self,text="Town2")
        town3Label = Button(self,text="Town3")
        town4Label = Button(self,text="Town4")

        faction1Label = Button(self,text="Faction1")
        faction2Label = Button(self,text="Faction2")


        #place label
        locationLabel.grid(row=1,column=1,columnspan = 3,sticky="nesw")

        #place headers
        factionsLabel.grid(row=2,column = 1,sticky="nesw")
        townsLabel.grid(row=2,column = 2,sticky="nesw")
        otherLabel.grid(row=2,column = 3,sticky="nesw")

        #place data
        town1Label.grid(row=3,column = 2,sticky="nesw")
        town2Label.grid(row=4,column = 2,sticky="nesw")
        town3Label.grid(row=5,column = 2,sticky="nesw")
        town4Label.grid(row=6,column = 2,sticky="nesw")

        faction1Label.grid(row=3,column = 1,sticky="nesw")
        faction2Label.grid(row=4,column = 1,sticky="nesw")
                
class TownFrame(tk.Frame):
    def __init__(self,container):
        super().__init__(container)
        #print("Town frame initialised")

        #configure grid
        Grid.columnconfigure(self,1,weight=1)
        Grid.columnconfigure(self,2,weight=1)
        Grid.columnconfigure(self,3,weight=1)

        Grid.rowconfigure(self,1,weight=1)
        Grid.rowconfigure(self,2,weight=1)
        Grid.rowconfigure(self,3,weight=1)
        Grid.rowconfigure(self,4,weight=1)
        Grid.rowconfigure(self,5,weight=1)
        Grid.rowconfigure(self,6,weight=1)


        

        #Location Label
        location = "funtown"
        locationLabel =Label(self,text="You are in " + location)
        
        #Headers
        townInfoLabel = Label(self,text="Info",bg="grey")
        peopleLabel = Label(self,text="People",bg="grey")
        buildingsLabel = Label(self,text="Buildings",bg="grey")

        #Town Info
        factionLabel = Label(self,text="faction: human")
        townTypeLabel = Label(self,text="Type: city")
        townSizeLabel = Label(self,text="Size: 10")
        mayorLabel = Label(self,text="Mayor: Mr Mannory")

        #People 
        person1Label = Button(self,text="Person1")
        person2Label = Button(self,text="Person2")
        person3Label = Button(self,text="Person3")
        person4Label = Button(self,text="Person4")

        #Buildings
        building1Label = Button(self,text="Building1")
        building2Label = Button(self,text="Building2")
        building3Label = Button(self,text="Building3")
        building4Label = Button(self,text="Building4")

        #place everything
        locationLabel.grid(row=1,column=1,columnspan=3,sticky="nsew")

        townInfoLabel.grid(row=2,column=1,sticky="nsew")
        peopleLabel.grid(row=2,column=2,sticky="nsew")
        buildingsLabel.grid(row=2,column=3,sticky="nsew")

        factionLabel.grid(row=3,column=1,sticky="nsew")
        townTypeLabel.grid(row=4,column=1,sticky="nsew")
        townSizeLabel.grid(row=5,column=1,sticky="nsew")
        mayorLabel.grid(row=6,column=1,sticky="nsew")

        person1Label.grid(row=3,column=2,sticky="nsew")
        person2Label.grid(row=4,column=2,sticky="nsew")
        person3Label.grid(row=5,column=2,sticky="nsew")
        person4Label.grid(row=6,column=2,sticky="nsew")

        building1Label.grid(row=3,column=3,sticky="nsew")
        building2Label.grid(row=4,column=3,sticky="nsew")
        building3Label.grid(row=5,column=3,sticky="nsew")
        building4Label.grid(row=6,column=3,sticky="nsew")

class ShopFrame(tk.Frame):
    def __init__(self,container):
        super().__init__(container)
        #print("Shop frame initialised")

        #Configure Grid
        Grid.columnconfigure(self,1,weight=1)
        Grid.columnconfigure(self,2,weight=1)
        Grid.columnconfigure(self,3,weight=1)

        Grid.rowconfigure(self,1,weight=1)
        Grid.rowconfigure(self,2,weight=1)
        Grid.rowconfigure(self,3,weight=1)
        Grid.rowconfigure(self,4,weight=1)

        #Location Label
        location = "shop"
        locationLabel =Label(self,text="You are in " + location)

        #Info Header
        infoLabel =Label(self,text="info",bg="grey")
        
        #Info Data
        shopnameLabel =Label(self,text="shop")
        ownerLabel =Label(self,text="owner: garosh")
        typeLabel =Label(self,text="type: shop")
        staffLabel =Label(self,text="staff: 2")
        
        #Actions Header

        #Actions data

        #place everything
        locationLabel.grid(row=1,column=1,columnspan=3,sticky="nsew")

        infoLabel.grid(row=2,column=1,sticky="nsew")

        shopnameLabel.grid(row=3,column=1,sticky="nsew")
        ownerLabel.grid(row=4,column=1,sticky="nsew")
        typeLabel.grid(row=5,column=1,sticky="nsew")
        staffLabel.grid(row=6,column=1,sticky="nsew")
        