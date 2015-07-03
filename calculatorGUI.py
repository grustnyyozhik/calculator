__author__ = ''

from Tkinter import *
import calculatorFrame


class CalculatorGUI(object):

    def __init__(self):
        self.root = Tk()
        self.root.title("Calculator")
        self.root.resizable(0, 0)
        self.menu = self.createMenu(self.root)
        self.calculator = calculatorFrame.CalculatorFrame(self.root)
        self.calculator.pack()

    def createMenu(self, win):
        topMenu = Menu(win)
        win.config(menu=topMenu)
        topMenu.add_cascade(label='View', underline=0)
        return topMenu

    def show(self):
        self.root.mainloop()
