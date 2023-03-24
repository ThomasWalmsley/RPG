

class Game():
	turn = 0
	def __init__(self):
		print("game made")
		turn = 0
	def update():
		pass
	def on_step(self):
		#here is the game loop, this should run every turn
		self.turn = self.turn +1
		print ("turn : " + str(self.turn))
		pass
	def game_print(self,message):
		print(message)