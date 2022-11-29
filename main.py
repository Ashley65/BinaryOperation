import inquirer
import questionary
from pprint import pprint

i = int(input("Enter the first number: "))
j = int(input("Enter the second number: "))
print("This is the first number: ", i)
print("This is the second number: ", j)
print("Here a list of available operations")
print("'AND', 'OR', 'NAND', 'XOR', 'XNOR'")
answers = str(input("Enter the particular operation: "))
options = [inquirer.List('operation', message="what is your particular operation ",
                         choices=['AND', 'OR', 'NAND', 'XOR', 'XNOR']), ]
answers = inquirer.prompt(options)

pprint(answers)


def userPick():
    if answers['operation'] == 'AND':
        print("Output of ", i, " AND ", j, "is", AND(i, j))
    elif answers['operation'] == 'OR':
        print("Output of ", i, " OR ", j, "is", OR(i, j))
    elif answers['operation'] == 'NAND':
        print("Output of ", i, " NAND ", j, "is", NAND(i, j))


def AND(i, j):
    return i & j


def OR(i, j):
    return i | j


def NOT(i):
    return ~i + 2


def NAND(i, j):
    return NOT(AND(i, j))


def XOR(i, j):
    return i ^ j


def XNOR(i, j):
    return NOT(XOR(i, j))


print("Output of ", i, " AND ", j, "is", AND(i, j))
print("Output of ", i, " OR ", j, "is", OR(i, j))
print("Output of ", i, " NANT ", j, "is", NAND(i, j))
print("Output of ", i, " XOR ", j, "is", XOR(i, j))
print("Output of ", i, " XNOR ", j, "is", XNOR(i, j))
