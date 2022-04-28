import tkinter as tk

class GUI():

    window = tk.Tk()
    input = tk.IntVar()
    nextText = tk.StringVar()
    box = tk.Text(window)
    scroller = tk.Scrollbar(window)

    def getButtonOne(self):
        self.input = 1
        print("1")

    def getButtonTwo(self):
        self.input = 2
        print("2")

    def getButtonThree(self):
        self.input = 3
        print("3")
    
    def advance(self):
        self.printText(self.getNextText)

    buttonOne = tk.Button(window, text = "1", command = getButtonOne)
    buttonTwo = tk.Button(window, text = "2", command = getButtonTwo)
    buttonThree = tk.Button(window, text = "3", command = getButtonThree)
    buttonNext = tk.Button(window, text = "Next", command = advance)
    

    def __init__(self):
        print("GUI INITIALIZED")
        self.window.grid_propagate(False)
        self.window.grid_rowconfigure(0, weight = 1)
        self.window.grid_columnconfigure(0, weight=1)
        self.box.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        self.box['yscrollcommand'] = self.scroller.set
        self.box.configure(state = 'disabled')
        self.scroller.grid(row=0, column =1, sticky='nsew')
        


    def getInput(self):
        return self.input
    
    def assemble(self):
        print("GUI STARTED")
        
        self.buttonOne.grid(row = 1,column = 0)
        self.buttonTwo.grid(row = 2,column = 0)
        self.buttonThree.grid(row = 3,column = 0)
        self.buttonNext.grid(row = 4,column = 3)

    def start(self):
        self.window.mainloop()
    
    def printText(self, message):
        self.box.insert(tk.END, message)
    
    def update(self):
        self.box.update()

    def setNextText(self, nextText):
        self.nextText = nextText
    
    def getNextText(self):
        return self.nextText