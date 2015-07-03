__author__ = ''
import operator

class Calculation(object):

    def __init__(self):
        self.expression = []
        self.exp_numbers = []
        self.exp_operators = []
        self.operators = {'+': operator.add, '-': operator.sub, '/': operator.div, '*': operator.mul}
        self.priority = {'+': 0, '-': 0, '/': 1, '*': 1}


    def calculate(self, expression):
        """
        :param math expression to be calculated
        :return: result of calculation

        1. if expression ends with . add 0  :  1+2. => 1+2.0
        2. parse expression to 2 stacks : stack with numbers and stack with operators
            parse runs in accordance to rules of infix without parentheses
        3. if after parse operators still remained in the stack
        pop operator and 2 numbers, operate and push result tu stack of numbers till
        operators stack is empty
        4. result is the remaining element in the numbers stack
        """
        first =0
        second = 0
        if expression[-1] == '.':
            expression += '0'
        self.expression[:0] = expression
        self.__parse()
        try:
            while self.exp_operators:
                op = self.exp_operators.pop()
                func = self.operators[op]
                first = self.exp_numbers.pop()
                second = self.exp_numbers.pop()
                self.exp_numbers.append(func(first, second))
        except ZeroDivisionError:
            self.__clear()
            raise
        else:
            res = self.exp_numbers.pop()
            self.__clear()
            return res

    def __clear(self):
        """
        clear all the lists after calculation
        """
        self.expression = []
        self.exp_numbers = []
        self.exp_operators = []

    def __append_by_priority(self, op):
        while self.exp_operators and self.priority[self.exp_operators[-1]] > self.priority[op]:
                prev_op = self.exp_operators[-1]
                first = self.exp_numbers.pop()
                second = self.exp_numbers.pop()
                func = self.operators[prev_op]
                self.exp_numbers.append(func(first, second))
                self.exp_operators.pop()

        self.exp_operators.append(op)


    def __parse(self):
        temp = ''
        for i in self.expression[::-1]:
            if i == ' ':
                self.exp_operators.pop()
                self.exp_numbers.append(-1*(self.exp_numbers.pop()))
            elif i in self.operators.keys():
                if temp != "":
                    self.exp_numbers.append(float(temp))
                    temp = ""
                self.__append_by_priority(i)
            else:
                temp = i + temp

        if temp != "":
            self.exp_numbers.append(float(temp))
        if self.expression[0] == '-':
            self.exp_operators.pop()
            self.exp_numbers.append(-1*(self.exp_numbers.pop()))