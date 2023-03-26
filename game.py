import json

class Game():
	gameName = ""
	turn = 0
	playerCharacter = None
	actions = {}

	def __init__(self):
		print("game made")
		self.gameName = "game1"
		self.turn = 0
		self.playerCharacter = "tom"
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

	def writeToJSONFile(self,path,fileName,data):
		filePathNameWExt = './GameSaves/' + fileName + '.json'
		with open(filePathNameWExt, 'w') as fp:
			json.dump(data,fp)

	def new_game(self):
		print("new game")
	def save_game(self):
		print("save game")
		gamedata = {"gameName":self.gameName,"playerCharacter":self.playerCharacter,"turn":self.turn}
		self.writeToJSONFile('./GameSaves/',self.gameName,gamedata)
	def load_game(self):
		print("load game")