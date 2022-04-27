from Character import Character

class Party:
    roster = []
    partyLen = 0

    def __init__(self):
        wizard = Character(4, 3, 3, "Wizard")
        fighter = Character(3, 4, 3, "Fighter")
        thief = Character(3, 3, 4, "Thief")
        self.roster = [wizard, fighter, thief]
        self.partyLen = len(self.roster)
    
    def getRoster(self):
        return self.roster
    
    def getPartyLen(self):
        return self.partyLen
    
    #sort function
    def sortingKey(self, e):
        return e.getInitiative()

    #roll initiative for all characters, order them,  and print out the order
    def rollInitiative(self):
        #for every character in the initiative
        for x in self.roster:
            #roll their initiative
            x.rollInitiative()
    
        #sort the roster by the sorting function (by initiative)
        self.roster.sort(key = self.sortingKey)

        #place holders for flavor
        count = 1
        suffix = None
        #determines the correct suffix and prints out the order
        for x in self.roster:
            #sets the correct suffix
            if(count == 1):
                suffix = "st"
            elif (count == 2):
                suffix = "nd"
            elif (count == 3):
                suffix = "rd"
            else:
                suffix = "th"
            #prints out the order
            print(x.getName() + " is " + str(count) + suffix + " place in combat order!")
            #increments the counter
            count += 1
    
    def rollPartyInitiative(self):
        sum = 0
        for x in self.roster:
            sum += x.rollInitiative()
        sum = sum/len(self.roster)
        return sum

    def characterTurn(self, x, monster):
        if(x.getHealth() > 0):
            print( x.getName() + "'s turn!\n1: magic attack\n2: pysical attack\n3: heal")
            #choose: 1 = magic, 2 = physical, 3 = heal
            actionInput = int(input())

            #if magic
            if(actionInput == 1):
                #find how much damage spell does
                dam = monster.takeDamage(x.doMagicDamage())
                #if the spell does 0 or less damage
                if(dam <= 0):
                    print("There was no effect!")
                    #if the spell does more than 0 damage
                elif(dam > 0):
                    print("You cast a spell!")
                    print("You deal " + str(dam) + " points of damage!")
                    print("You have " + str(x.getEnergy()) + " magical energy left!")
                    #if the monster is at 0 health, end loop
                    if(monster.getHealth() <= 0):
                        print("Monster defeated!\n")
                        return 1
                            
                    
            #if physical
            elif(actionInput == 2):
                #find how much damage the attack does
                dam = monster.takeDamage(x.doPhysicalDamage())
                #if the damage is 0 or less
                if(dam <= 0):
                    print("You deal 0 points of damage!")
                    print("There was no effect!")
                    #if the damage is more than 0
                elif(dam > 0):
                    print("You throw a punch!")
                    print("You deal " + str(dam) + " points of damage!")
                    #if the monster is at 0 health, end loop
                    if(monster.getHealth() <= 0):
                        print("Monster defeated!\n")
                        return 1

            #if heal
            elif(actionInput ==3):
                print("Select a target:")
                #z = counter
                z = 1
                #for each character in the roster
                for y in self.roster:
                    #print counter: name (ex "1: fighter")
                    print(str(z) + ": " + y.getName())
                    #increment counter
                    z += 1
                #grab player choice
                choice = int(input())
                #correct player choice
                choice -= 1
                #call heal on that character
                healVal = x.heal(self.roster[choice])
                if(healVal > -1):
                    print(self.roster[choice].getName() + " ate a senzu bean!")
                    print(self.roster[choice].getName() + " healed for " + str(healVal) + " points of healing!")
                    print(x.getName() + " has " + str(x.getBeans()) + " senzu beans left!")
                else:
                    print(x.getName() + " has " + str(x.getBeans()) + " senzu beans left!")
                    print(x.getName() + " can't heal " + self.roster[choice].getName() + "!") 
                #if the monster is at 0 health, end loop (backup)
                if(monster.getHealth() <= 0):
                    print("Monster defeated!\n")
                    return 1
        return 0