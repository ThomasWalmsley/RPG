import tkinter as tk
from tkinter import *
from tkinter import ttk


class StartScreenFrame(tk.Frame):
    def __init__(self,container):
        super().__init__(container)

        #configure grid
        Grid.rowconfigure(self,0,weight=1)
        Grid.rowconfigure(self,1,weight=1)
        Grid.rowconfigure(self,2,weight=1)
        Grid.rowconfigure(self,3,weight=1)
        Grid.columnconfigure(self,2,weight=1)

        #create buttons
        #regarding continue, this button should be hidden if there are no saves stored
        continueButton = Button(self,text="Continue",command =lambda:self.buttonClick("continue"))
        newGameButton = Button(self,text="New Game",command =lambda:self.buttonClick("newgame"))
        LoadGameButton = Button(self,text="Load Game",command =lambda:self.buttonClick("load"))
        exitButton = Button(self,text="Exit",command =lambda:self.buttonClick("exit"))
        
        #place buttons
        continueButton.grid(row=0,column=2,sticky="nsew")
        newGameButton.grid(row=1,column=2,sticky="nsew")
        LoadGameButton.grid(row=2,column=2,sticky="nsew")
        exitButton.grid(row=3,column=2,sticky="nsew")

    def buttonClick(self,action):
        action = action
        if action == "exit":
            exit()
        if action == "continue":
            print("continue")
            #game.continue
        else:
            self.master.switchFrame(action)
        
class LoadScreenFrame(tk.Frame):
    def __init__(self,container):
        super().__init__(container)

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

        #setup grid
        #self.columnconfigure(2,1)
        #self.rowconfigure(2,1)

        #label Create New World

        #label enter world name
        # TextBox Creation
        self.inputtxt = tk.Text(self,
            height = 5,
            width = 10)
        #self.inputtxt.pack()
        self.inputtxt.grid(column=1, row=1,)
        
        #world options
        #radio button - population high/low

        #Button Create New World
        createNewWorldButton = Button(self,text="Create",command = self.create_new_world)
        createNewWorldButton.grid(column=1, row=2,)
    def retrieve_input(self):
        input = self.inputtxt.get("1.0",'end-1c')
    def create_new_world(self):
        worldName = self.retrieve_input()
        self.master.action("new")
             








   
class WorldFrame(tk.Frame):
    def __init__(self,container):
        super().__init__(container)
        print("World frame initialised")

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
        #configure grid
        #Grid.columnconfigure(self,1,weight=1)
        #Grid.columnconfigure(self,2,weight=1)
        #Grid.columnconfigure(self,3,weight=1)
        #Grid.columnconfigure(self,4,weight=1)
        #Grid.columnconfigure(self,5,weight=1)
        #Grid.columnconfigure(self,6,weight=1)
        #Grid.rowconfigure(self,1,weight=1)
        #Grid.rowconfigure(self,2,weight=1)
        #Grid.rowconfigure(self,3,weight=1)
       # Grid.rowconfigure(self,4,weight=1)
        #Grid.rowconfigure(self,5,weight=1)
        #Grid.rowconfigure(self,6,weight=1)
        


        #create widgets
        #landButton= Button(self,text="Area",command =None)
        #townButton = Button(self,text="Town",command =None)
        #buildingButton = Button(self,text="Shop",command =None)
        #locationLabel = Label(self,text="You are in Fred's Shop")
        #dividerLabel = Label(self,text="",bg="blue")
        #talkButton = Button(self,text="Talk to Fred",command =None)
        #shopButton = Button(self,text="Shop",command =None)

        #place widgets
        #landButton.grid(row=1,column=1,sticky="nesw")
        #townButton.grid(row=1,column=2,sticky="nesw")
        #buildingButton.grid(row=1,column=3,sticky="nesw")
        #locationLabel.grid(row=2,column=1,columnspan=6,sticky="nesw")
        #dividerLabel.grid(row=3,column=3)
        #talkButton.grid(row=4,column=3)
        #shopButton.grid(row=5,column=3)

class AreaFrame(tk.Frame):
    def __init__(self,container):
        super().__init__(container)
        print("Area frame initialised")

        #Location Label
        location = "area"
        locationLabel =Label(self,text="You are in " + location)

        #place widgets
        locationLabel.grid(row=1,column=1,columnspan = 4)

class TownFrame(tk.Frame):
    def __init__(self,container):
        super().__init__(container)
        print("Town frame initialised")

class ShopFrame(tk.Frame):
    def __init__(self,container):
        super().__init__(container)
        print("Shop frame initialised")





class CharacterFrame(tk.Frame):
    def __init__(self,container):
        super().__init__(container)
        print("Character frame initialised")
        #self.master.config(bg = "red")
        #self.config(background = "blue")
        #characterPortraitButton = Button(self,text="Face",command =None,padx=20,pady=10)

        #configure grid
        Grid.rowconfigure(self,1,weight=1)    
        Grid.rowconfigure(self,2,weight=1)
        Grid.rowconfigure(self,3,weight=1)
        Grid.rowconfigure(self,4,weight=1)
        Grid.rowconfigure(self,5,weight=1)
        Grid.rowconfigure(self,6,weight=1) 
        Grid.rowconfigure(self,7,weight=1) 
        Grid.rowconfigure(self,8,weight=1) 
        
        Grid.columnconfigure(self,1,weight=1)
        Grid.columnconfigure(self,2,weight=1)

        #create widgets
        characterPortraitButton = Button(self,text="Face",command =None)
        funnyLabel = Label(self,text="Character")
        characternameLabel = Label(self,text ="Name")
        ageLabel = Label(self,text="Age")
        actionPointsLabel = Label(self,text="Action Points")
        statsLabel = Label(self,text="stats")
        raceLabel = Label(self,text="race")
        religionLabel = Label(self,text="religion")
        

        #place widgets
        #column 1
        characterPortraitButton.grid(row=1,column = 1, rowspan=2, sticky="nesw")
        characternameLabel.grid(row=3,column = 1, rowspan=1, sticky="nesw")
        ageLabel.grid(row=4,column = 1, rowspan=1, sticky="nesw")
        actionPointsLabel.grid(row=5,column = 1, rowspan=1, sticky="nesw")
        statsLabel.grid(row=6,column = 1, rowspan=1, sticky="nesw")
        raceLabel.grid(row=7,column = 1, rowspan=1, sticky="nesw")
        religionLabel.grid(row=8,column = 1, rowspan=1, sticky="nesw")
        
        #column 2
        funnyLabel.grid(row=1,column=2,rowspan=6,sticky="nesw")



        
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

    def action(self,action):
        #print(action)
        self.game.do_action(action)

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
            #load most recent save and start game

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