__author__ = ''
from Tkinter import *
import calculation
import UnaryOperationsLib

class CalculatorFrame(Frame):

    def __init__(self, root, **options):
        Frame.__init__(self, root, options)
        self.grid()
        self.currValue = ''
        self.buttonsList = [

            '1', '2', '3', '4', '5', '6',
            '7', '8', '9', '0', 'C', 'CE', '+',
            '-', '/', '*', u"\u221A", '+/-', '%', '.', '='
        ]
        self.binOpList = ['+', '-', '/', '*', ]
        self.unOpList = {u"\u221A": UnaryOperationsLib.square_operation, '+/-': UnaryOperationsLib.negate_operation, '%': UnaryOperationsLib.percent_operation}
        self.data = StringVar()
        self.addElements()
        self.logic = calculation.Calculation()
        self.to_clear = False

    def addElements(self):
        """
        The function adds buttons to the calculator frame
        """

        self.data.set('0')
        self.entryDataTxtBox = Entry(self, textvariable=self.data, bd=25, width=40, state=DISABLED, font=30, justify="right")
        self.entryDataTxtBox.grid(row=0, column=0, columnspan=3)

        j = 0
        for i in range(len(self.buttonsList)):
            if i % 3 == 0:
                j += 1
            btn = Button(self, text=self.buttonsList[i], padx=15, pady=15, width=15, bd=5, relief=RAISED, fg='black')
            btn.grid(row=j, column=i % 3)
            if self.buttonsList[i] == 'C':
                btn.config(command=self.clear)
            elif self.buttonsList[i] == 'CE':
                btn.config(command=self.clear_last)
            elif self.buttonsList[i] == '=':
                btn.config(command=lambda: self.calculate(self.data.get()))
            else:
                # btn.config(command=lambda txt=self.buttonsList[i]: self.data.set(self.data.get() + txt))
                btn.config(command=lambda x=self.buttonsList[i]: self.updateExpression(x))
                # second possible solution


    def get_result(self, expression):
        try:
            res = self.logic.calculate(expression)
            if res < 0:
                self.currValue = ' ' + str(-1*res)
            else:
                self.currValue = str(res)
        except ZeroDivisionError:
            raise
        else:
            return res

    def calculate(self, expression):
        """
        The function calculating result after pressing button =
        """
        if self.to_clear:   #clear dispalay after error
            self.clear()
            self.to_clear = False
        op = None

        if expression[-1] in self.binOpList:   # if the expression ends with operator e.g  1+2*  =>  (1+2)*(1+2)
            op = expression[-1]
            expression = expression[:-1]
        try:
            res = self.get_result(expression)
        except ZeroDivisionError:
            self.data.set("Zero Division Error")
            self.to_clear = True
        else:
            if op:
                new_expression = " " + str(res) + op + " " + str(res) if res < 0 else str(res) + op + str(res)
                try:
                    res = self.get_result(new_expression)
                except ZeroDivisionError:
                    self.data.set("Zero Division Error")
                    self.to_clear = True
                else:
                    if res.is_integer():
                        res = int(res)
                    self.data.set(str(res))
            else:
                if res.is_integer():
                    res = int(res)
                self.data.set(str(res))
            self.currValue = ' ' + str(res) if res < 0 else str(res)


    def updateExpression(self, val):
        """
        The function updates math expression after pressing on number or operation buttons of calculator
        """
        if self.to_clear:
            self.clear()
            self.to_clear = False

        temp = self.data.get()

        if val in self.binOpList:   # if pressed +, -, /, *
            if temp[-1] in self.binOpList:
                temp = temp[:-1] + val
            else:
                if temp[-1] == '.':
                    temp += '0'
                temp += val
            self.currValue = ''

        elif val in self.unOpList.keys():  # if pressed %, root, +/- buttons
            temp, self.currValue = self.unOpList[val](temp, self.currValue)

        elif val == '.':   # if pressed the float button
            if val not in self.currValue:
                if temp[-1] in self.binOpList:
                    temp += '0'
                    self.currValue += '0'
                temp += val
                self.currValue += val
        else:  # if pressed number buttons
            if temp == '0':
                temp = val
                self.currValue = val
            elif temp[-1] == '0' and temp[-2] in self.binOpList:
                temp = temp[:-1] + val
                self.currValue = val
            else:
                temp += val
                self.currValue += val
        self.data.set(temp)  # update display text


    def clear(self):
        """
        function clears display after pressing C button
        """
        self.data.set("0")
        self.currValue = '0'

    def clear_last(self):
        """
        function clears last value on the display after pressing CE button
        """
        if self.to_clear:
            self.clear()
            self.to_clear = False
        else:
            temp = self.data.get()
            temp = temp[:-len(self.currValue)]
            self.currValue = '' if temp else '0'
            self.data.set(temp if temp else '0')



