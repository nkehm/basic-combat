from Party import Party 
from Monsters import Monsters
import threading

class Battle:
    #The readout for the GUI
    text = "peen"
    #The user input from the GUI
    input = -1
    #The monster object
    monsterOBJ = Monsters()
    #The individual monster that the party is fighting
    monster = monsterOBJ.getMonster()
    #The party object
    partyOBJ = Party()
    #The party of player characters (an array of character objects)
    party  = partyOBJ.getRoster()
    #A long string representation of the monster and party members hp's
    health = ""
    #waiting event
    e = threading.Event()


    def __init__(self):
        print("Battle Initialized")

    def getText(self):
        return self.text

    def getHealth(self):
        self.updateHealth()
        return self.health

    def setInput(self, input):
        self.input = input
        return input

    def setText(self, text):
        self.text = text
        return text

    def setE(self):
        self.e.set() 

    def clearE(self):
        self.e.clear()

    def newMonster(self):
        self.monster = self.monsterOBJ.createRandomMonster()

    def updateHealth(self):
        retString = ""
        for x in self.party:
            retString += x.getName() + " HP: " + str(x.getHealth()) + "\n"
        retString += self.monster.getName() + " HP: " + str(self.monster.getHealth())
        self.health = retString

    def start(self):
        print("Battle Started")
        #flag for starting game
        go = 0
        #fight number counter
        fightCount = 0
        #starts battle
        while go == 0:
            self.e.wait()
            self.clearE()
            print("F")
            self.setText("Round: " + str(fightCount) + "\n")
            self.e.wait()
            self.clearE()
            print("W")
            #while the monster is alive
            while self.monster.getHealth()>0 and go == 0:
                #flag for if the party goes first (True) or the monster goes first (False)
                initiative = self.rollOff()
                if(initiative == True):
                    self.partyTurn()
                    self.monsterTurn()
                else:
                    self.monsterTurn()
                    self.partyTurn()
                go =1
    
    def rollOff(self):
        print("rolled")

    def partyTurn(self):
        print("party turn")
    
    def monsterTurn(self):
        print("monster turn")
                