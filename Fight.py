import random
from Character import Character

monsterSmall = Character(3, 3, 3, "Small")
monsterMedium = Character(5, 5, 5, "Medium")
monsterLarge = Character(10, 10, 10, "Large")
monsters = [monsterSmall, monsterMedium, monsterLarge]
monster = None

wizard = Character(5, 2, 2, "Wizard")
fighter = Character(2, 5, 2, "Fighter")
thief = Character(2, 2, 5, "Thief")
roster = [wizard, fighter, thief]



def fightExample():
    for x in roster:
        x.getStats()

    i = 1

    while i == 1:
        monster = monsters[random.randint(0,2)]
        round = 1
        while monster.getHealth() > 0:
            print("round: " + str(round))
            healthCheck(monster)
            for x in roster:
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
                #if heal
                elif(actionInput ==3):
                    print("Select a target:")
                    #z = counter
                    z = 1
                    #for each character in the roster
                    for y in roster:
                        #print counter: name (ex "1: fighter")
                        print(str(z) + ": " + y.getName())
                        #increment counter
                        z += 1
                    #grab player choice
                    choice = int(input())
                    #correct player choice
                    choice -= 1
                    #call heal on that character
                    healVal = x.heal(roster[choice])
                    print("You gave " + roster[choice].getName() +" a senzu bean!")
                    print(roster[choice].getName() + " healed for " + str(healVal) + " points of healing!")
                print()
            #monster randomly selects an action
            #choose: 1 = magic, 2 = physical, 3 = heal
            #monsterChoice = random.randint(1,3)
            monsterChoice = 2
            #monster randomly selects a target
            target = roster[random.randint(0,2)]
            #if magic
            if(monsterChoice == 1):
                #calculate damage of spell
                dam = target.takeDamage(x.doMagicDamage())
                print(monster.getName() + " casts a spell at " + target.getName() +"!")
                #if damage is 0 or less
                if(dam <= 0):
                    print("There was no effect!")
                #if damage is greater than 0
                elif(dam > 0):
                    print(monster.getName() + " deals " + target.getName() + " " + str(dam) + " points of damage!")
            #if physical
            elif(monsterChoice == 2):
                #calculate damage
                dam = target.takeDamage(x.doPhysicalDamage())
                #damage report (TURN OFF LATER)
                print("damage(dam)!! " + str(dam))
                print(monster.getName() + " attacks " + target.getName() + "!")
                #if damage is 0 or less
                if(dam <= 0):
                    print(monster.getName() + " deal 0 points of damage!")
                    print("There was no effect!")
                #if damage greater than 0
                elif(dam > 0):
                    print(monster.getName() + " hits " + target.getName() + "!")
                    print(monster.getName() + " deals " + str(dam) + " points of damage!")
            #if heal
            elif(monsterChoice == 3):
                #monster heals itself
                healVal = monster.heal(monster)
                print(monster.getName() + " ate a senzu bean!")
                print(monster.getName() + " healed for " + str(healVal) + " points of healing!")
            #increment round counter
            round += 1
        print("end1")
    print("end2")

def healthCheck(monster):
    print(monster.getName() + " HP: " + str(monster.getHealth()))
    print(wizard.getName() + " HP: " + str(wizard.getHealth()))
    print(fighter.getName() + " HP: " + str(fighter.getHealth()))
    print(thief.getName() + " HP: " + str(thief.getHealth()))
    print()
    
fightExample()
