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
        #a game should not be created here
        #self.game=Game(self,3)
        #self.save_game()
        self.load_options()
        if not self.confirm_latest_save():
            self.latest_save = ""
        #self.get_all_save_games()

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
        elif message == "get all save games":
            response = self.get_all_save_games()
        elif message.startswith('loadgame'):
            gamefile = message[9:]
            self.load_game(gamefile)#
        elif message == "save":
            self.save_game()
        elif message.startswith('create world'):
            name = message[13:]
            self.create_game(name)
        return response

    def request2(self,request):
        if not request:
            print("request made but no request found")
            return
        requestType = request.type
        requestData = request.data
        requesttypes = {
            "change state":"hi",
            "get":"",
            "set":"",
            "load":"",
            "save":"",
            "create":""
        }

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

    def load_game(self,gamename):
        gamefile = gamename
        #if gamename doesn't have .json at the end, add it
        if not (gamefile.endswith('.json')):
            gamefile = gamefile+'.json'
        #check the file exists
        directoryPath = './Saves/'
        saveFileExists = False
        for path in os.scandir(directoryPath):
            if path.name == gamefile:
                saveFileExists = True    
        if not saveFileExists:
            print("save file not found")
            return
        #read file 
        path = './Saves/'+gamefile
        file = open(path)
        data = json.load(file)
        file.close()
        #delete any previous game
        if self.game:
            del self.game
        #create game 
        self.game = Game(self,data)
        #update options
        self.latest_save = self.game.name + '.json'
        self.save_options()
        #print for testing
        print(data)

    def save_game(self): 
        if not self.game:
            print("cannot save, no game")
            return
        print("save game")
        data = self.game.to_json()
        json_string = json.dumps(data,indent=4)
        filePathName = './Saves/' + self.game.name + '.json'
        with open(filePathName,'w')as outfile:
            outfile.write(json_string)

        self.latest_save = self.game.name + '.json'
        self.save_options()

    def create_game(self,data):
        #delete any existing game
        if self.game:
            del self.game
        self.game = Game(self,data)
        print(self.game.name)
        if self.game:
            self.save_game()

    def load_options(self):
        directoryPath = './'
        optionsFileExists = False
        for path in os.scandir(directoryPath):
            if path.name == 'options.json':
                optionsFileExists = True    
        if not optionsFileExists:
            print("no options file found")
            return 
        file = open('options.json')
        data = json.load(file)
        self.latest_save=data["latest_save"]
        print(self.latest_save)
        #for i in data:
            #print(i)
        file.close()

    def get_all_save_games(self):
        directoryPath = './Saves/'
        if os.listdir(directoryPath) == []:
            print("No saves found") 
            return
        savesList = []
        for path in os.scandir(directoryPath):
            if path.is_file():
                savesList.append(path.name)
                print(path.name + " appended")
        return savesList        