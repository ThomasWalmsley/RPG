from .Race import Race
from .Sex import Sex
import json

class Character():
    #simple things
    id:int
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
    
    def __init__(self,id,name,age,sex,race,maxActionPoints,maxHealth):
        self.id = id
        self.name = name
        self.age = age
        self.sex = sex
        self.race = race
        self.maxActionPoints = maxActionPoints
        self.maxHealth = maxHealth

    def to_json(self):
        return {
            "id":self.id,
            "name":self.name,
            "age":self.age,
            "sex":str(self.sex),
            "race":str(self.race),
            "maxActionPoints":self.maxActionPoints,
            "maxHealth":self.maxHealth,           
        }
    