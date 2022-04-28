import threading
import time
from Fight import Fight
from GUI import GUI

gui = GUI()
fight = Fight()

def guiStart():
    gui.assemble()
    gui.start()

def fightStart():
    fight.fightExample()

timerStart = time.perf_counter()

def wait():
    time.sleep(2)
    print("waited")

""""
threadExampleA = threading.Thread(target=wait)
threadExampleB = threading.Thread(target=wait)
threadExampleC = threading.Thread(target=wait)

threadExampleA.start()
threadExampleB.start()
threadExampleC.start()

#wait()
#wait()
#wait()


timerEnd = time.perf_counter()
print("Time elapsed: " + str(timerStart-timerEnd))
"""



threadFight = threading.Thread(target = fightStart)
guiStart()

threadFight.start()