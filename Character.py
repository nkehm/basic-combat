import random

class Character:    
#  stats = [brain, muscle, spirit]
#  health = muscle*2
#  energy = brain*2
#  defense = (muscle * .5) + (brain * .5)
    stats = [0, 0, 0]
    initiative = 0
    energy = stats[0] * 2
    health = stats[1] * 2
    defense = stats[2] *2
    beans = 0
    name = None
    
    def __init__(self, newBrain, newMuscle, newSpirit, newName):
        self.stats = [newBrain, newMuscle, newSpirit]
        self.energy = newBrain * 2
        self.health = newMuscle * 2
        self.defense = newSpirit * 2
        self.beans = 3
        self.name = newName
###############################################################################
    def updateStats(self, newBrain, newMuscle, newSpirit):
        self.stats = [newBrain, newMuscle, newSpirit]
        self.energy = newBrain * 2
        self.health = newMuscle * 2
        self.defense = newSpirit * 2
###############################################################################
    def getHealth(self):
        return self.health
    
    def getEnergy(self):
        return self.energy
    
    def getDefense(self):
        return self.defense
    
    def getBrain(self):
        return self.stats[0]
    
    def getMuscle(self):
        return self.stats[1]
    
    def getSpirit(self):
        return self.stats[2]
    
    def getInitiative(self):
        return self.initiative

    def getName(self):
        return self.name

    def getBeans(self):
        return self.beans

    def getStats(self):
        print("health: " + str(self.getHealth()) + " energy: " +
         str(self.getEnergy()) + " defense: " + str(self.getDefense()) + " brain: " +
          str(self.getBrain()) + " muscle: " + str(self.getMuscle()) + " spirit: " +
           str(self.getSpirit()) + " name: " + self.getName())
###############################################################################
    def setBrain(self, newBrain):
        self.stats = [newBrain, self.stats[1], self.stats[2]]
        
    def setMuscle(self, newMuscle):
        self.stats = [self.stats[0], newMuscle, self.stats[2]]
        
    def setSpirit(self, newSpirit):
        self.stats = [self.stats[0], self.stats[1], newSpirit]

    def setName(self, newName):
        self.name = newName
###############################################################################
    def doMagicDamage(self):
        damSum = 0
        if(self.energy > 0):
            for x in range(self.stats[0]):
                damSum += random.randint(0,self.stats[0]) + self.stats[0]
            self.energy -= 1
        else:
            print(self.name + " is out of magical energy!"+ self.name +" can't cast a spell!")
        
        return damSum

    def doPhysicalDamage(self):
        damSum = 0
        for x in range(self.stats[1]):
            damSum += random.randint(0,self.stats[1]) + self.stats[1]
        return damSum

    def heal(self, target):
        healVal = -1
        if(self.beans > 0):
            healVal = random.randint(1, self.stats[2])
            target.health += healVal
            self.beans -= 1 
        else:
            print(self.name + " is out of beans!")
        return healVal

    def takeDamage(self, damageTaken):
        damageRecieved = damageTaken - self.defense
        if(damageRecieved > 0):
            self.health -= damageRecieved
        return damageRecieved

    def rollInitiative(self):
        self.initiative = random.randint(1, 6)# + self.stats(1)
###############################################################################
    def brainCheck(self):
        result = random.randint(0,10)
        if(result < self.stats[0]):
            return True
        else:
            return False

    def muscleCheck(self):
        result = random.randint(0,10)
        if(result < self.stats[1]):
            return True
        else:
            return False

    def spiritiCheck(self):
        result = random.randint(0,10)
        if(result < self.stats[2]):
            return True
        else:
            return False
###############################################################################
    def levelUp(self, selection):
        self.stats[selection] += 1
