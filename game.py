import json
#from Data import *
from GameData.Race import Race
from GameData.Sex import Sex
from GameData.Character import Character

class Game():
	#gameData = None
	gameName = ""
	turn = 0
	playerCharacter = None
	actions = {}

	def __init__(self,controller):
		print("game made")
		self.controller = controller
		self.gameName = "game1"
		self.turn = 0
		self.playerCharacter = self.create_character()
		#print(gameData["gameName"])
		self.actions = {
		"new":self.new_game,
		"save":self.save_game,
		"load":self.load_game
		
		}

	def update():
		pass

	def on_step(self):
		#here is the game loop, this should run every turn
		self.turn = self.turn +1
		print ("turn : " + str(self.turn))
		pass

	def game_print(self,message):
		print(message)

	def do_action(self,action):
		print("doing action : "+action)
		if action in self.actions:
			self.actions[action]()
			#self.actions[action]()

	def create_character(self):
		character =Character("Tom",22,Sex.Male,Race.Human,5,100)
		#self.save_character(character)







	def writeToJSONFile(self,path,fileName,data):
		filePathNameWExt = './Saves/' + fileName + '.json'
		with open(filePathNameWExt, 'w') as fp:
			json.dump(data,fp)

	def new_game(self):
		print("new game")
		#create player character
		
		#generate area
		#generate factions
		#generate towns
		#generate characters


	def save_character(self,character):
		print("save character")
		#json_string = json.dumps(character.toJson(),indent=4)	
		json_string = json.dumps(character.__dict__,indent=4)	
		filePathName = './Saves/' + "character" + '.json'
		with open(filePathName,'w')as outfile:
			outfile.write(json_string)		

	def save_game(self):
		print("save game")
		data = {"game name":self.gameName,"player character":self.playerCharacter,"turn":self.turn}
		json_string = json.dumps(data)
		filePathName = './Saves/' + self.gameName + '.json'
		with open(filePathName,'w')as outfile:
			outfile.write(json_string)
		#gamedata = {"gameName":self.gameName,"playerCharacter":self.playerCharacter,"turn":self.turn}
		#gamedata = self
		#self.writeToJSONFile('./Data/Saves/',self.gameName,gameData)


	def load_game(self):
		print("load game")