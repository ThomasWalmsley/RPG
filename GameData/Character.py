from .Race import Race
from .Sex import Sex
import json

class Character():
    #simple things
    name:str
    age:int
    sex:Sex
    race:Race
    actionPoints:int
    maxActionPoints:int
    health:int
    maxHealth:int

    #complex things
    #religion:Religion
    #faction:Faction
    equipment:dict
    skills:dict
    spells:dict

    #stats
    strength:int
    dexterity:int
    intelligence:int
    contitution:int
    magicka:int
    
    def __init__(self,name,age,sex,race,maxActionPoints,maxHealth):
        self.name = name
        self.age = age
        self.sex = sex
        self.race = race
        self.maxActionPoints = maxActionPoints
        self.maxHealth = maxHealth

    #def toJson(self):
        #return json.dumps(self, default=lambda o: o.__dict__)
    