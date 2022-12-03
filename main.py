from pprint import pprint

i = int(input("Enter the first number: "))
j = int(input("Enter the second number: "))
print("This is the first number: ", i)
print("This is the second number: ", j)
print("Here a list of available operations")
print("'AND', 'OR', 'NAND', 'XOR', 'XNOR'")
answers = str(input("Enter the particular operation: "))


def userPick():  #
    if answers.upper() == 'AND':
        print("Output of ", i, " AND ", j, "is", AND(i, j))
    elif answers.upper() == 'OR':
        print("Output of ", i, " OR ", j, "is", OR(i, j))
    elif answers.upper() == 'NAND':
        print("Output of ", i, " NAND ", j, "is", NAND(i, j))
    elif answers.upper() == 'XOR':
        print("Output of ", i, " XOR ", j, "is", XOR(i, j))
    elif answers.upper() == 'XNOR':
        print("Output of ", i, " XNOR ", j, "is", XNOR(i, j))


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


pprint(userPick())
