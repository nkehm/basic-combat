import threading
from Fight import Fight
from GUI import GUI

gui = GUI()
fight = Fight()

def guiStart():
    gui.assemble()
    gui.start()

def fightStart():
    fight.fightExample()

#guiStart()
threadGui = threading.Thread(target = guiStart)
threadFight = threading.Thread(target = fightStart)

threadGui.start()
threadFight.start()