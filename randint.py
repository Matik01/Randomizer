import random
from tkinter import Label, Entry, Button
import tkinter as tk

class Application():
    def __init__(self):
        self.main = tk.Tk()
        self.resultEntry = Entry(self.main, text='result')
        self.leftValue = Entry(self.main, text='firstValue')
        self.rightValue = Entry(self.main, text='rightValue')
        self.startButton = Button(self.main, text='Generate', width=25, command=self.doRandom)

    def start(self):
        self.main.mainloop()

    def pack(self):
        Label(self.main, text="Result:").pack()
        self.resultEntry.pack()

        Label(self.main, text="Left value:").pack()
        self.leftValue.pack()

        Label(self.main, text="Right value:").pack()
        self.rightValue.pack()

        self.startButton.pack()
        

    def doRandom(self):
        a = int(self.leftValue.get())
        b = int(self.rightValue.get())
        
        result = random.randint(a, b)

        resultLength = len(self.resultEntry.get())
        self.resultEntry.delete(0, resultLength)
        self.resultEntry.insert(0, result)

app = Application()
app.pack()
app.start()
