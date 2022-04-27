import random
from Character import Character

class Monsters:
    monster = None
    
    def __init__(self):
        self.createRandomMonster()
    
    def getMonster(self):
        return self.monster
    
    def setMonster(self, monster):
        self.monster = monster
    
    def createRandomMonster(self):
        brain = random.randint(1,5)
        muscle = random.randint(1,5)
        spirit = random.randint(1,5)
        sum = brain + muscle +spirit
        
        if (sum  < 5):
            name = "easy"
        elif (sum < 11 and sum > 4):
            name = "medium"
        else:
            name = "hard"
        self.monster = Character(brain, muscle, spirit, name)

    def makeTargetChoice(self, partyOBJ):
        highHealthRoster = []
        for x in partyOBJ.getRoster():
            if (x.getHealth() > 10):
                highHealthRoster.append(x)
        if(len(highHealthRoster) > 0):
            print
            return highHealthRoster[random.randint(0,len(highHealthRoster)-1)]
        else:
            return partyOBJ.getRoster()[random.randint(0,partyOBJ.getPartyLen()-1)]

    def makeActionChoice(self):
        if(self.monster.getHealth() < 10 and self.monster.getBeans() > 0):
            return 3
        else:
            if(self.monster.getBrain() > self.monster.getMuscle() and self.monster.getEnergy() > 0):
                return 1
            else:
                return 2

    def monsterTurn(self, newMonster, roster):
        monster = newMonster
        #monster randomly selects an action
        #choose: 1 = magic, 2 = physical, 3 = heal
        monsterChoice = self.makeActionChoice()
        #monster randomly selects a target
        target = self.makeTargetChoice(roster)
        if(monster.getHealth() > 0):
            #if magic
            if(monsterChoice == 1):
                #calculate damage of spell
                dam = target.takeDamage(monster.doMagicDamage())
                print(monster.getName() + " casts a spell at " + target.getName() +"!")
                #if damage is 0 or less
                if(dam <= 0):
                    print("There was no effect!")
                    #if damage is greater than 0
                elif(dam > 0):
                    print(monster.getName() + " deals " + target.getName() + " " + str(dam) + " points of damage!")
                    if(target.getHealth() <= 0):
                        roster.remove(target)

            #if physical
            elif(monsterChoice == 2):
                #calculate damage
                dam = target.takeDamage(monster.doPhysicalDamage())
                print(monster.getName() + " attacks " + target.getName() + "!")
                #if damage is 0 or less
                if(dam <= 0):
                    print(monster.getName() + " deal 0 points of damage!")
                    print("There was no effect!")
                    #if damage greater than 0
                elif(dam > 0):
                    print(monster.getName() + " hits " + target.getName() + "!")
                    print(monster.getName() + " deals " + str(dam) + " points of damage!")
                    if(target.getHealth() <= 0):
                        roster.remove(target)

            #if heal
            elif(monsterChoice == 3):
                #monster heals itself
                healVal = monster.heal(monster)
                if(healVal > -1):
                    print(monster.getName() + " ate a senzu bean!")
                    print(monster.getName() + " healed for " + str(healVal) + " points of healing!")
                    print(monster.getName() + " has " + str(monster.getBeans()) + " senzu beans left!")
                else:
                    print(monster.getName() + " has " + str(monster.getBeans()) + " senzu beans left!")
                    print(monster.getName() + " can't heal!")    
            
            print()
            return roster.getRoster()