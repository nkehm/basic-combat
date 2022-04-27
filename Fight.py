#imports
import random
from Character import Character
from Monsters import Monsters

#global refrence for monster
monster = None

#sample characters for demo
wizard = Character(4, 3, 3, "Wizard")
fighter = Character(3, 4, 3, "Fighter")
thief = Character(3, 3, 4, "Thief")
roster = [wizard, fighter, thief]

monsterOBJ = Monsters()

#begin demo fight
def fightExample():
    #flag to start (or stop) another fight
    i = 1
    #fight counter
    fight = 1
    #monsters slain counter
    monsterCounter = 0 
    while i == 1:
        #print the fight number ("Fight: 1")
        print("Fight: " + str(fight))
        #initialize all of the demo monsters
        monster = monsterOBJ.getMonster()
        

        #roll the initiative of the players and sort them
        rollInitiative()

        #round counter
        round = 1

        #while the monster is not dead and there is at least one living party member
        while (monster.getHealth() > 0 and len(roster) > 0):
            #print the round number ("Round: 1")
            print("Round: " + str(round))
            #print out the monster's and the character's healths
            healthCheck(monster)
            
            #monster's turn
            monsterTurn(monster, monsterOBJ)
            
            #holding variable to be used for multiple checks
            temp = 0
            #for each character in the roster
            for x in roster:
                #character x takes their turn
                temp = characterTurn(x, monster)
                #increase the monsters killed counter by the number of monsters slain
                monsterCounter += temp
                #if the monster was killed, stop cycling through player turns
                if(temp == 1):
                    break
                
                print()
            #increment round counter
            round += 1

        #if all of the party members are dead
        if(len(roster) == 0):
            print("You lost! You killed " + str(monsterCounter) + " monsters!")
            #end the biggest loop
            i=2
            #break the current loop
            break
        else:
            monsterOBJ.setRandomMonster()
            print("Good job! You have killed " + str(monsterCounter) + " monster(s) so far!")
            print("1 to continue, 2 to quit")
            #1 to continue big loop, 2 to stop it
            i = int(input())
            print()
        
        #increment fight counter
        fight += 1
        

def healthCheck(monster):
    print(monster.getName() + " HP: " + str(monster.getHealth()))
    print(wizard.getName() + " HP: " + str(wizard.getHealth()))
    print(fighter.getName() + " HP: " + str(fighter.getHealth()))
    print(thief.getName() + " HP: " + str(thief.getHealth()))
    print()

def monsterTurn(newMonster, monsterOBJ):
    monster = newMonster
    #monster randomly selects an action
    #choose: 1 = magic, 2 = physical, 3 = heal
    monsterChoice = random.randint(1,3)
    #monster randomly selects a target
    target = monsterOBJ.makeTargetChoice(roster)
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

def characterTurn(x,monster):
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
            if(healVal > -1):
                print(roster[choice].getName() + " ate a senzu bean!")
                print(roster[choice].getName() + " healed for " + str(healVal) + " points of healing!")
                print(x.getName() + " has " + str(x.getBeans()) + " senzu beans left!")
            else:
                print(x.getName() + " has " + str(x.getBeans()) + " senzu beans left!")
                print(x + " can't heal " + roster[choice].getName() + "!") 
            #if the monster is at 0 health, end loop (backup)
            if(monster.getHealth() <= 0):
                print("Monster defeated!\n")
                return 1
    return 0

#sort function
def sortingKey(e):
    return e.getInitiative()

#roll initiative for all characters, order them,  and print out the order
def rollInitiative():
    #for every character in the initiative
    for x in roster:
        #roll their initiative
        x.rollInitiative()
    
    #sort the roster by the sorting function (by initiative)
    roster.sort(key = sortingKey)

    #place holders for flavor
    count = 1
    suffix = None
    #determines the correct suffix and prints out the order
    for x in roster:
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

fightExample()