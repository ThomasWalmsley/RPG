import json
#from Data import *
from GameData.Race import Race
from GameData.Sex import Sex
from GameData.Character import Character

class Game():
	name = ""
	turn = 0
	playerCharacter = None

	def __init__(self,controller,data):
		print("game made")
		self.controller = controller
		if data:
			self.initialise(data)
		else:
			self.name = "default"
		self.turn = 0
		self.playerCharacter = self.create_character()

	def initialise(self,data):
		if isinstance(data,str):
			self.name = data
		else:
			#self.name = data['name']
			self.name = data['name']
		print("name = "+self.name)

	def to_json(self):
		return {
			"name":self.name,
			"turn":self.turn,
			"playercharacter":self.playerCharacter.to_json()         ,   
			
		}

	def on_step(self):
		#here is the game loop, this should run every turn
		self.turn = self.turn +1
		print ("turn : " + str(self.turn))
		pass

	def create_character(self):
		character =Character(1,"Tom",22,Sex.Male,Race.Human,5,100)
		#self.save_character(character)
		return character
