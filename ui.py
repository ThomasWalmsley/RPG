from tkinter import *
2
class Window(Frame):
	def increase_turn(self):
		self.turnLabel["text"] = "turn increased"

	def __init__(self, master=None,game = None):
		Frame.__init__(self, master)        
		self.master = master
		self.game =game
		self.game.game_print("game printing")
		# widget can take all window
		self.pack(fill=BOTH, expand=1)
		#stop dashed line appearing in menu
		self.master.option_add('*tearOff', False)
		
		#menu
		menu=Menu(self.master)
		self.master.config(menu=menu)
		#submenues
		fileMenu = Menu(menu)
		menu.add_cascade(label="Menu", menu=fileMenu)
		#characterMenu = Menu(menu)
		#menu.add_cascade(label="Character", menu=characterMenu)
		#worldMenu = Menu(menu)
		#menu.add_cascade(label="World", menu=worldMenu)
		
		menu.add_command(label="Character",command=self.print)
		menu.add_command(label="World",command=self.print)

		#submenu items
		fileMenu.add_command(label="New", command=self.print)
		fileMenu.add_command(label="Save", command=self.print)
		fileMenu.add_command(label="Load", command=self.print)
		fileMenu.add_command(label="Exit", command=self.clickExitProgram)
		
		#create label
		self.turnLabel= Label(self,text = str(self.game.turn))
		self.turnLabel.place(x=90,y=90)
		
		# create button, link it to clickExitProgram()
		exitButton = Button(self, text="Exit", command=self.clickExitProgram)
		#cmdButton = Button(self, text="End Turn",command=self.endTurn)
		cmdButton = Button(self, text="End Turn",command=self.endTurn)
        # place button at (0,0)
		exitButton.place(x=0, y=0)
		cmdButton.place(x=0, y=100)
		

	def clickExitProgram(self):
		exit()
	def print(self):	
		print("print")
	def endTurn(self):
		self.game.on_step()
		turn_num = self.game.turn
		self.turnLabel["text"] = str(turn_num)
        
