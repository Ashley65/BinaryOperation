from pprint import pprint

i = int(input("Enter the first number: "))
j = int(input("Enter the second number: "))
# The line below will show the user what their number will be in binary
print("This is the first number in binary is : ", bin(i)[2:])
print("This is the second number: ",  bin(j)[2:])
print("Here a list of available operations")
print("'AND', 'OR', 'NAND', 'XOR', 'XNOR'")
answers = str(input("Enter the particular operation: "))


def userPick():  #
    if answers.upper() == 'AND':
        print("Output of ", i, " AND ", j, "is", bin(AND(i, j)))
    elif answers.upper() == 'OR':
        print("Output of ", i, " OR ", j, "is", bin(OR(i, j)))
    elif answers.upper() == 'NAND':
        print("Output of ", i, " NAND ", j, "is", bin(NAND(i, j)))
    elif answers.upper() == 'XOR':
        print("Output of ", i, " XOR ", j, "is", bin(XOR(i, j)))
    elif answers.upper() == 'XNOR':
        print("Output of ", i, " XNOR ", j, "is", bin(XNOR(i, j)))


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
