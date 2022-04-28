#imports
from Monsters import Monsters
from Party import Party
import threading

class Fight:

    #global refrence for monster
    monster = None
    roster = []
    #sample characters for demo
    e = threading.Event()
    input = None

    monsterOBJ = Monsters()
    partyOBJ = Party()

    actionLine = ""
    characterLine = ""
    


    def __init__(self,):
        print("Fight Initialized")
    
    def getActionLine(self):
        return self.actionLine
    
    def setActionLine(self, text):
        self.actionLine = text

    def getCharacterLine(self):
        return self.characterLine
    
    def setCharacterLine(self, text):
        self.characterLine = text
    
    def getMonster(self):
        return self.monster
    
    def getPartyOBJ(self):
        return self.partyOBJ

    def set(self, input):
        self.input = input

    
    def setE(self):
        self.e.set() 

    def clearE(self):
        self.e.clear()

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
            #initialize the demo monster
            self.monsterOBJ.createRandomMonster()
            self.monster = self.monsterOBJ.getMonster()
            self.healthCheck(self.monster,self.partyOBJ)
            #print the fight number ("Fight: 1")
            self.setActionLine("Fight: " + str(fight))
            self.e.wait()
            self.clearE()


            #roll the initiative of the players and sort them
            self.setActionLine(self.partyOBJ.rollInitiative())
            self.e.wait()
            self.clearE()

            #round counter
            round = 1

            #while the monster is not dead and there is at least one living party member
            while (self.monster.getHealth() > 0 and self.partyOBJ.getPartyLen() > 0):
                #print the round number ("Round: 1")
                self.setActionLine("Round: " + str(round))
                self.e.wait()
                self.clearE()
                self.roster = self.partyOBJ.getRoster()
                #print out the monster's and the character's healths
                self.healthCheck(self.monster,self. partyOBJ)
                #partyInitiative = self.partyOBJ.rollPartyInitiative()
                #monsterInitiative = self.monster.rollInitiative()
                monsterInitiative = 1
                partyInitiative = 0
                if(monsterInitiative > partyInitiative):
                    self.setActionLine("The monster moves first!")
                    self.e.wait()
                    self.clearE()
                    #monster's turn
                    arr = self.monsterOBJ.monsterTurn(self.monster, self.partyOBJ)
                    self.setActionLine(arr[0][0])
                    self.e.wait()
                    self.clearE()
                    self.roster = arr[1]

                    #holding variable to be used for multiple checks
                    temp = 0
                    #for each character in the roster
                    for x in self.roster:
                        #character x takes their turn
                        if(x.getHealth() > 0):
                            self.setActionLine( x.getName() + "'s turn!\n1: magic attack\n2: pysical attack\n3: heal")
                            self.e.wait()
                            self.clearE()
                            temp = self.partyOBJ.characterTurn(self.input, x, self.monster)
                            print("Next: ")
                            print(temp[0])
                            self.setActionLine(temp[0])
                            self.e.wait()
                            self.e.clear()
                            #increase the monsters killed counter by the number of monsters slain
                            monsterCounter += int(temp[1])
                            #if the monster was killed, stop cycling through player turns
                            if(temp[1] == 1):
                                break
                            self.setActionLine("\n")
                            self.e.wait()
                            self.clearE()

                else:
                    self.setActionLine("The party was faster!")
                    self.e.wait()
                    self.clearE()
                    #holding variable to be used for multiple checks
                    temp = 0
                    #for each character in the roster
                    for x in self.roster:
                        #character x takes their turn
                        temp = self.partyOBJ.characterTurn(x, self.monster)
                        self.setActionLine(temp[0])
                        self.e.wait()
                        self.e.clear()
                        #increase the monsters killed counter by the number of monsters slain
                        monsterCounter += temp[1]
                        #if the monster was killed, stop cycling through player turns
                        if(temp[1] == 1):
                            break
                        self.setActionLine("\n")
                        self.e.wait()
                        self.clearE()

                    #monster's turn
                    arr = self.monsterOBJ.monsterTurn(self.monster, self.partyOBJ)
                    self.roster = arr[0][1]
                #increment round counter
                round += 1

            #if all of the party members are dead
            if(self.partyOBJ.getPartyLen == 0):
                self.setActionLine("You lost! You killed " + str(monsterCounter) + " monsters!")
                self.e.wait()
                self.clearE()
                #end the biggest loop
                i=2
                #break the current loop
                break
            else:
                self.setActionLine("Good job! You have killed " + str(monsterCounter) + " monster(s) so far!")
                self.e.wait()
                self.clearE()
                self.setActionLine("1 to continue, 2 to quit")
                self.e.wait()
                self.clearE()
                #1 to continue big loop, 2 to stop it
                i = int(input())
                self.setActionLine("\n")
                self.e.wait()
                self.clearE()

            #increment fight counter
            fight += 1


    def healthCheck(self, monster, partyOBJ):
        var = ""
        var += (monster.getName() + " HP: " + str(monster.getHealth()) + "\n")
        for x in partyOBJ.getRoster():
            var += (x.getName() + " HP: " + str(x.getHealth()) + "\n")
        self.setCharacterLine(var)
        self.e.wait()
        self.clearE()
