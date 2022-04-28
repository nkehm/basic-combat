import tkinter as tk

class GUI():

    window = tk.Tk()
    input = tk.IntVar()
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

    buttonOne = tk.Button(window, text = "1", command = getButtonOne)
    buttonTwo = tk.Button(window, text = "2", command = getButtonTwo)
    buttonThree = tk.Button(window, text = "3", command = getButtonThree)
    

    def __init__(self):
        print("GUI INITIALIZED")

    def getInput(self):
        return self.input
    
    def assembleAndStart(self):
        print("GUI STARTED")
        self.window.grid_propagate(False)
        self.window.grid_rowconfigure(0, weight = 1)
        self.window.grid_columnconfigure(0, weight=1)
        self.box.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        self.scroller.grid(row=0, column =1, sticky='nsew')
        self.box['yscrollcommand'] = self.scroller.set

        self.buttonOne.grid(row=1,column=0)
        self.buttonTwo.grid(row=2,column=0)
        self.buttonThree.grid(row=3,column=0)

        self.window.mainloop()

gui = GUI()
gui.assembleAndStart()
print(gui.getInput)