# package calculator

from math import exp, nan
from enum import Enum


# A calculator for rather simple arithmetic expressions.
# Your task is to implement the missing functions so the
# expressions evaluate correctly. Your program should be
# able to correctly handle precedence (including parentheses)
# and associativity - see helper functions.
# The easiest way to evaluate infix expressions is to transform
# them into postfix expressions, using a stack structure.
# For example, the expression 2*(3+4)^5 is first transformed
# to [ 3 -> 4 -> + -> 5 -> ^ -> 2 -> * ] and then evaluated
# left to right. This is known as Reverse Polish Notation,
# see: https://en.wikipedia.org/wiki/Reverse_Polish_notation
#
# NOTE:
# - You do not need to implement negative numbers
#
# To run the program, run either CalculatorREPL or CalculatorGUI

MISSING_OPERAND:  str = "Missing or bad operand"
DIV_BY_ZERO:      str = "Division with 0"
MISSING_OPERATOR: str = "Missing operator or parenthesis"
OP_NOT_FOUND:     str = "Operator not found"
OPERATORS:        str = "+-*/^"

class TooManyParenthesis(IndexError):
    pass

class MissingOperator(IndexError):
    pass

def infix_to_postfix(expression):
    output_stack, operator_stack = [], []
    for token in expression:
        try:
            if token_is_a_number(token):
                output_stack.append(token)
            elif token in OPERATORS or token == "(":
                if add_to_operator_stack_condition(operator_stack, token):
                    operator_stack.append(token)
                elif get_precedence(token) <= get_precedence(operator_stack[-1]):
                    output_stack.append(operator_stack.pop())
                    operator_stack.append(token)
            elif token == ")":
                output_stack, operator_stack = pop_operators_in_paranthises(output_stack, operator_stack)
        except TooManyParenthesis as error:
            print(repr(error))
            break
    while len(operator_stack) > 0:
        output_stack.append(operator_stack.pop())
    return output_stack

def pop_operators_in_paranthises(output_stack, operator_stack):
    try:
        while operator_stack[-1] != ")":
            op = operator_stack.pop()
            output_stack.append(op)
    except IndexError:
        raise TooManyParenthesis(MISSING_OPERATOR)

    return output_stack, operator_stack

def add_to_operator_stack_condition(operator_stack, token):
    return len(operator_stack) == 0 or token == "(" or \
        operator_stack[-1] == "(" or \
            get_precedence(token) > get_precedence(operator_stack[-1]) or \
                get_associativity(token) == Assoc.RIGHT

# -----  Evaluate RPN expression -------------------
def eval_postfix(postfix_tokens):
    try:
        evaluation_stack = []
        while len(postfix_tokens) > 0:
            token = postfix_tokens.pop(0)
            if token not in OPERATORS:
                evaluation_stack.append(float(token))
            else:
                try:
                    evaluation_stack = pop_and_calculate_from_stack(evaluation_stack, token)
                except ZeroDivisionError:
                    print(DIV_BY_ZERO)
                    break
        return evaluation_stack[0] 
    except MissingOperator as error:
        print(repr(error))
    except ValueError:
        print(MISSING_OPERAND)


def pop_and_calculate_from_stack(evaluation_stack, token):
    try:
        operand1 = evaluation_stack.pop()
        operand2 = evaluation_stack.pop()
        result = apply_operator(token, int(operand1), int(operand2))
        if result == nan:
            raise ZeroDivisionError
        else:
            evaluation_stack.append(result)
        return evaluation_stack
    except IndexError:
        raise MissingOperator(OP_NOT_FOUND)

# Method used in REPL
def eval_expr(expr: str):
    if len(expr) == 0:
        return nan
    try:
        tokens = tokenize(expr)
        postfix_tokens = infix_to_postfix(tokens)
        return eval_postfix(postfix_tokens)
    except ValueError:
        print()

def apply_operator(op: str, d1: float, d2: float):
    op_switcher = {
        "+": d1 + d2,
        "-": d2 - d1,
        "*": d1 * d2,
        "/": nan if d1 == 0 else d2 / d1,
        "^": d2 ** d1
    }
    return op_switcher.get(op, ValueError(OP_NOT_FOUND))


def get_precedence(op: str):
    op_switcher = {
        "+": 2,
        "-": 2,
        "*": 3,
        "/": 3,
        "^": 4
    }
    return op_switcher.get(op, ValueError(OP_NOT_FOUND))


class Assoc(Enum):
    LEFT = 1
    RIGHT = 2


def get_associativity(op: str):
    if op in "+-*/":
        return Assoc.LEFT
    elif op in "^":
        return Assoc.RIGHT
    else:
        return ValueError(OP_NOT_FOUND)


# ---------- Tokenize -----------------------
def tokenize(expr: str):
    tokenized_list = []
    full_number = ""
    for char in expr:
        if token_is_not_a_number(char):
            if full_number != "":
                tokenized_list.append(full_number)
            tokenized_list.append(char)
            full_number = ""
        elif token_is_a_number(char):
            full_number += char
    if full_number != "":
        tokenized_list.append(full_number)
    return tokenized_list


def token_is_a_number(token):
    return token not in OPERATORS and token not in "()"
  
def token_is_not_a_number(token):
    return token in OPERATORS or token in "()"
'''
def Test():
    expression = input("Input Expression: ")
    output_stack, operator_stack,  = [], []
    for token in expression:
        if token not in OPERATORS and token not in "()":
            output_stack.append(token)
        elif token in OPERATORS or token == "(":
            if len(operator_stack) == 0 or token == "(" or operator_stack[-1] == "(" or get_precedence(token) > get_precedence(operator_stack[-1]) or get_associativity(token) == Assoc.RIGHT:
                operator_stack.append(token)
            elif get_precedence(token) <= get_precedence(operator_stack[-1]):
                output_stack.append(operator_stack.pop())
                operator_stack.append(token)
        elif token == ")":
            for i in range(len(operator_stack)):
                op = operator_stack.pop()
                if op == "(":
                    break
                output_stack.append(op)
    while len(operator_stack) > 0:
        output_stack.append(operator_stack.pop())

    evaluation_stack = []
    while len(output_stack) > 0:
        token = output_stack.pop(0)
        if token not in OPERATORS:
            evaluation_stack.append(token)
        else:
            operand1 = evaluation_stack.pop()
            operand2 = evaluation_stack.pop()
            result = apply_operator(token, int(operand1), int(operand2))
            evaluation_stack.append(result)
    print(result)  
'''
