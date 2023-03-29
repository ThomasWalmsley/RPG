import json
#from Data import *
from GameData.Race import Race
from GameData.Sex import Sex
from GameData.Character import Character

class Game():
	name = ""
	turn = 0
	playerCharacter = None

	def __init__(self,controller):
		print("game made")
		self.controller = controller
		self.name = "game3"
		self.turn = 0
		self.playerCharacter = self.create_character()


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
		character =Character("Tom",22,Sex.Male,Race.Human,5,100)
		#self.save_character(character)
		return character
