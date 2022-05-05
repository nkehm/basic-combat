import random
from Character import Character

class Monsters:
    monster = None
    
    def __init__(self):
        self.createRandomMonster()
        print("Monster Initialized")
    
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
        return self.getMonster()

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
        #arr -> [[String to be print out], roster]
        arr = [[""],[]]
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
                arr[0][0] = (monster.getName() + " casts a spell at " + target.getName() +"!"+ "\n")
                #if damage is 0 or less
                if(dam <= 0):
                    arr[0][0] += ("There was no effect!"+ "\n")
                    #if damage is greater than 0
                elif(dam > 0):
                    arr[0][0] += (monster.getName() + " deals " + target.getName() + " " + str(dam) + " points of damage!"+ "\n")
                    if(target.getHealth() <= 0):
                        roster.remove(target)

            #if physical
            elif(monsterChoice == 2):
                #calculate damage
                dam = target.takeDamage(monster.doPhysicalDamage())
                arr[0][0] = (monster.getName() + " attacks " + target.getName() + "!"+ "\n")
                #if damage is 0 or less
                if(dam <= 0):
                    arr[0][0] += (monster.getName() + " deal 0 points of damage!"+ "\n")
                    arr[0][0] += ("There was no effect!"+ "\n")
                    #if damage greater than 0
                elif(dam > 0):
                    arr[0][0] += (monster.getName() + " hits " + target.getName() + "!"+ "\n")
                    arr[0][0] += (monster.getName() + " deals " + str(dam) + " points of damage!"+ "\n")
                    if(target.getHealth() <= 0):
                        roster.remove(target)

            #if heal
            elif(monsterChoice == 3):
                #monster heals itself
                healVal = monster.heal(monster)
                if(healVal > -1):
                    arr[0][0] = (monster.getName() + " ate a senzu bean!")
                    arr[0][0] += (monster.getName() + " healed for " + str(healVal) + " points of healing!" + "\n")
                    arr[0][0] += (monster.getName() + " has " + str(monster.getBeans()) + " senzu beans left!"+ "\n")
                else:
                    arr[0][0] = (monster.getName() + " has " + str(monster.getBeans()) + " senzu beans left!"+ "\n")
                    arr[0][0] += (monster.getName() + " can't heal!")    
            
            arr[0][0] += "\n"
            arr[1] = roster.getRoster()
            return arr