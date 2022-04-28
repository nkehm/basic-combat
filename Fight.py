#imports
from Monsters import Monsters
from Party import Party

class Fight:

    #global refrence for monster
    monster = None
    roster = []
    #sample characters for demo


    monsterOBJ = Monsters()
    partyOBJ = Party()

    def __init__(self):
        print("Fight Initialized")

    #begin demo fight
    def fightExample(self):
        print("Fight Started")
        self.roster = self.partyOBJ.getRoster()
        #flag to start (or stop) another fight
        i = 1
        #fight counter
        fight = 1
        #monsters slain counter
        monsterCounter = 0 
        while i == 1:
            #print the fight number ("Fight: 1")

            print("Fight: " + str(fight))
            #initialize the demo monster
            self.monsterOBJ.createRandomMonster()
            self.monster = self.monsterOBJ.getMonster()


            #roll the initiative of the players and sort them
            self.partyOBJ.rollInitiative()

            #round counter
            round = 1

            #while the monster is not dead and there is at least one living party member
            while (self.monster.getHealth() > 0 and self.partyOBJ.getPartyLen() > 0):
                #print the round number ("Round: 1")
                print("Round: " + str(round))
                self.roster = self.partyOBJ.getRoster()
                #print out the monster's and the character's healths
                self.healthCheck(self.monster,self. partyOBJ)
                partyInitiative = self.partyOBJ.rollPartyInitiative()
                monsterInitiative = self.monster.rollInitiative()
                if(monsterInitiative > partyInitiative):
                    print("The monster was faster!")
                    #monster's turn
                    self.roster = self.monsterOBJ.monsterTurn(self.monster, self.partyOBJ)

                    #holding variable to be used for multiple checks
                    temp = 0
                    #for each character in the roster
                    for x in self.roster:
                        #character x takes their turn
                        temp = self.partyOBJ.characterTurn(x, self.monster)
                        #increase the monsters killed counter by the number of monsters slain
                        monsterCounter += temp
                        #if the monster was killed, stop cycling through player turns
                        if(temp == 1):
                            break
                        print()

                else:
                    print("The party was faster!")
                    #holding variable to be used for multiple checks
                    temp = 0
                    #for each character in the roster
                    for x in self.roster:
                        #character x takes their turn
                        temp = self.partyOBJ.characterTurn(x, self.monster)
                        #increase the monsters killed counter by the number of monsters slain
                        monsterCounter += temp
                        #if the monster was killed, stop cycling through player turns
                        if(temp == 1):
                            break
                        print()

                    #monster's turn
                    self.roster = self.monsterOBJ.monsterTurn(self.monster, self.partyOBJ)
                #increment round counter
                round += 1

            #if all of the party members are dead
            if(self.partyOBJ.getPartyLen == 0):
                print("You lost! You killed " + str(monsterCounter) + " monsters!")
                #end the biggest loop
                i=2
                #break the current loop
                break
            else:
                print("Good job! You have killed " + str(monsterCounter) + " monster(s) so far!")
                print("1 to continue, 2 to quit")
                #1 to continue big loop, 2 to stop it
                i = int(input())
                print()

            #increment fight counter
            fight += 1


    def healthCheck(self, monster, partyOBJ):
        print(monster.getName() + " HP: " + str(monster.getHealth()))
        for x in partyOBJ.getRoster():
            print(x.getName() + " HP: " + str(x.getHealth()))
        print()