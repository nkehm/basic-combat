import tkinter as tk
import threading
#from Fight import Fight
from Battle import Battle


#fight = None
battle = None


window = tk.Tk()
input = None
nextText = None
actionBox = tk.Text(window)
characterBox = tk.Text(window)
scroller = tk.Scrollbar(window)
characterBox.insert('@0,0', "Character info here!")
actionBox.insert('@0,0', """Welcome to basic fighting program, or bfp for short!
Actions are going to be written in this box as they happen!
Character info is on the left!
When you need to make a decision, select one of the 3 numbered buttons below!
And press next to advance turns!""")

def startBattle():
    """global fight
    fight = Fight()
    fight.fightExample()"""
    global battle
    battle = Battle()
    battle.start()

battleThread = threading.Thread(target = startBattle)


def getButtonOne():
    global input
    input = 1
    print(str(input))

def getButtonTwo():
    global input
    input = 2
    print(str(input))

def getButtonThree():
    global input
    input = 3
    print(str(input))
    
def advance():
    setActionNextText(battle.getText())
    print(str(getNextText()))
    actionBox.insert(tk.END, str(getNextText()) + "\n")
    actionBox.update()
    battle.setE()
    characterBox.delete('@0,0',tk.END)
    characterBox.insert('@0,0',battle.getHealth())
    characterBox.update()

#def startFightThread():
#    "fightThread.start()"


buttonOne = tk.Button(window, text = "1", command = getButtonOne)
buttonTwo = tk.Button(window, text = "2", command = getButtonTwo)
buttonThree = tk.Button(window, text = "3", command = getButtonThree)
buttonNext = tk.Button(window, text = "Next", command = advance)
#buttonStart = tk.Button(window, text = "Start", command = startFightThread)
        


def getInput():
    return input

def getNextText():
    return nextText

def setActionNextText(text):
    """global nextText
    nextText = text
    actionBox.update()"""
    
def assemble():
    print("GUI Initialized")
    window.geometry("900x600")
    window.grid_propagate(False)
    window.grid_rowconfigure(0, weight = 1)
    window.grid_columnconfigure(0, weight=1)
    actionBox['yscrollcommand'] = scroller.set
    characterBox.grid(row = 0, column = 0, sticky="nsew", padx=2, pady=2)
    actionBox.grid(row = 0, column = 1, sticky="nsew", padx=2, pady=2)
    scroller.grid(row = 0, column = 2 , sticky='nsew')    
    buttonOne.grid(row = 1, column = 1)
    buttonTwo.grid(row = 2, column = 1)
    buttonThree.grid(row = 3, column = 1)
    #buttonStart.grid(row = 3, column = 0)
    buttonNext.grid(row = 3, column = 2)
    battleThread.start()

def start():
    print("GUI Started")
    window.mainloop()

def assembleAndStart():
    assemble()
    start()

assembleAndStart()