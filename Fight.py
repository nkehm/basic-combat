import random
from Character import Character

monsterSmall = Character(3, 3, 3, "Small")
monsterMedium = Character(5, 5, 5, "Medium")
monsterLarge = Character(7, 7, 7, "Large")
monsters = [monsterSmall, monsterMedium, monsterLarge]
monster = None

wizard = Character(5, 2, 2, "Wizard")
fighter = Character(2, 5, 2, "Fighter")
thief = Character(2, 2, 5, "Thief")
roster = [wizard, fighter, thief]



def fightExample():
    i = 1

    while i == 1:
        monster = monsters[random.randint(0,2)]
        counter = 1
        while monster.getHealth() > 0:
            print("round: " + str(counter))
            healthCheck(monster)
            for x in roster:
                print( x.getName() + "'s turn!\n1: magic attack\n2: pysical attack\n3: heal")
                actionInput = int(input())
                if(actionInput == 1):
                    monster.takeDamage(x.doMagicDamage())
                    print("You cast a spell!")
                elif(actionInput == 2):
                    monster.takeDamage(x.doPhysicalDamage())
                    print("You throw a punch!")
                elif(actionInput ==3):
                    print("Select a target:")
                    z = 1
                    for y in roster:
                        print(str(z) + ": " + y.getName())
                        z += 1
                    choice = int(input())
                    x.heal(roster[choice-1])
                    print("You gave " + roster[choice].getName() +" a senzu bean!")
                print()
            counter += 1

def healthCheck(monster):
    print(monster.getName() + " HP: " + str(monster.getHealth()))
    print(wizard.getName() + " HP: " + str(wizard.getHealth()))
    print(fighter.getName() + " HP: " + str(fighter.getHealth()))
    print(thief.getName() + " HP: " + str(thief.getHealth()))
    print()
    
fightExample()
