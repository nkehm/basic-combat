import random
from re import S
from Character import Character

class Monsters:
    monsterEasy = Character(1, 1, 1, "Easy")
    monsterMedium = Character(3, 3, 3, "Medium")
    monsterHard = Character(5, 5, 5, "Hard")
    monsterRoster = None
    monster = None
    
    def __init__(self):
        self.monsterRoster = [self.monsterEasy,self.monsterMedium, self.monsterHard]
        self.monster = self.monsterRoster[random.randint(0,2)]
    
    def getMonster(self):
        return self.monster

    def getMonsterRosterLength(self):
        return len(self.monsterRoster)
    
    def getSelectMonster(self, selection):
        return self.monsterRoster[selection]

    def getMonsterRoster(self):
        return self.monsterRoster
    
    def setRandomMonster(self):
        self.monster = self.monsterRoster[random.randint(0,len(self.monsterRoster)-1)]
        return self.monster
    
    def setMonster(self, monster):
        self.monster = monster

    def setMonsterRoster(self, monster):
        self.monsterRoster = [monster]
        self.setRandomMonster()
    
    def appendMonster(self, monster):
        self.monsterRoster.append(monster)
        self.setRandomMonster()
    
    def createRandomMonster(self):
        self.appendMonster(Character(random.randint(1,10), random.randint(1,10), random.randint(1,10), "Random Monster"))

    def makeTargetChoice(self, characterRoster):
        highHealthRoster = []
        for x in characterRoster:
            if (x.getHealth() > 5):
                highHealthRoster.append(x)
        if(len(highHealthRoster) > 0):
            return highHealthRoster[random.randint(0,len(characterRoster)-1)]
        else:
            return characterRoster[random.randint(0,len(characterRoster)-1)]

