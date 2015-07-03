__author__ = ''

import math

def negate_operation(expression, value_to_update):
    """

    :param expression: the math expression existing currently
    :param value_to_update: last number in the expression to change sign, like expression = '1+3', value_to_update = '3'
    :return: updated expression and value

    1. check that expression is not empty
    2. if it ends with . then add 0 e.g 6+8. => 6+8.0
    3 choice of right action depends upon current sign
    """
    func = None
    if value_to_update != "":
        if expression[-1] == '.':
            expression += '0'
            value_to_update += '0'

        if '.' in expression:
            func = float
        else:
            func = int

        if func(value_to_update) < 0:
            expression = expression[:-(len(value_to_update))] + str(-1*func(value_to_update))
            value_to_update = str(-1*func(value_to_update))
        elif func(value_to_update) > 0:
            expression = expression[:-(len(value_to_update))] + ' ' + str(-1*func(value_to_update))
            value_to_update = ' ' + str(-1*func(value_to_update))
            # abs(a-b)<0.00000001
    return expression, value_to_update


def square_operation(expression, value_to_update):
    """
    :param expression: the math expression existing currently
    :param value_to_update: last number in the expression to change sign, like expression = '1+3', value_to_update = '3'
    :return: updated expression and value

    1. check that expression is not empty
    2. if it ends with . then add 0 e.g 6+8. => 6+8.0
    3 find root if value >= 0 and make updates
    """
    if value_to_update != "":
        if expression[-1] == '.':
            expression += '0'
            value_to_update += '0'
        if float(value_to_update) >= 0:
            length = len(value_to_update)
            value_to_update = str(math.sqrt(float(value_to_update)))
            expression = expression[:-length] + value_to_update

    return expression, value_to_update




def percent_operation(expression, value_to_update):
    """
    :param expression: the math expression existing currently
    :param value_to_update: last number in the expression to change sign, like expression = '1+3', value_to_update = '3'
    :return: updated expression and value

    1. check that expression is not empty
    2. if it ends with . then add 0 e.g 6+8. => 6+8.0
    3 find given percent from 1 and make updates
    """
    if value_to_update != "":
        if expression[-1] == '.':
            expression += '0'
            value_to_update += '0'
        length = len(value_to_update)
        res = float(value_to_update)/100
        value_to_update = ' ' + str(res) if res < 0 else str(res)
        expression = expression[:-length] + value_to_update
    return expression, value_to_update


