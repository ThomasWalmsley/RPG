import os
import json
from game import Game
#The controller controls everything
#it handles communication between all components
#eg UI asks controller for information from Game

class Controller():
    game=None
    state = ""
    latest_save=""
    player_options=[]#unused

    def __init__(self):
        #load options
        self.state="start"
        #self.latest_save = self.check_saves_folder()
        self.game=Game(self)
        self.read_saves()
        #self.save_options()

    def request(self,message):
        #clients use this to make requests
        if message =="state":
            response = self.state
        elif message =="latestsave":
            response = self.latest_save
        return response

    def check_saves_folder(self):
        directoryPath = './Saves/'
        if os.listdir(directoryPath) == []:
            print("No saves found")
        else:
            print("Saves found")

    def read_saves(self):
        # get all files inside a specific folder
        directory_path = './Saves/'
        for path in os.scandir(directory_path):
            if path.is_file():
                print(path.name)

    def to_json(self):
        data={
            "latest_save":self.latest_save,
            "player_options":self.player_options
        }
        return data

    def save_options(self):
        data = self.to_json()
        json_string = json.dumps(data,indent=4)
        filePathName = './' + "options" + '.json'
        with open(filePathName,'w')as outfile:
            outfile.write(json_string)

    def load_game(self):
        pass

    def save_game(self): 
        print("save game")
        data = self.game.to_json()
        json_string = json.dumps(data,indent=4)
        self.latest_save = self.game.name + '.json'
        filePathName = './Saves/' + self.game.name + '.json'
        with open(filePathName,'w')as outfile:
            outfile.write(json_string)

    def load_options(self):
        file = open('options.json')
        data = json.load(file)
        self.latest_save=data["latest_save"]
        print(self.latest_save)
        #for i in data:
            #print(i)
        file.close()