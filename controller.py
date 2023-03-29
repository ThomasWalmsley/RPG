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
        self.game=Game(self)
        self.save_game()
        self.load_options()
        if not self.confirm_latest_save():
            self.latest_save = ""
        #self.save_options()

    def request(self,message):
        #clients use this to make requests
        response =""
        if message =="state":
            response = self.state
        elif message =="latestsave":
            if self.confirm_latest_save():
                response = self.latest_save
        elif message == "changestate started":
            self.state = "started"
            print("state changed to started")
        return response

    def confirm_latest_save(self):
        directoryPath = './Saves/'
        if os.listdir(directoryPath) == []:
            print("No saves found") 
            return
        latest_save_exists = False
        for path in os.scandir(directoryPath):
            if path.name == self.latest_save:
                latest_save_exists = True
                #print("latest save exists")
        return latest_save_exists

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
        self.latest_save = self.game.name + '.json'

    def save_game(self): 
        if not self.game:
            print("cannot save, no game")
            return
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