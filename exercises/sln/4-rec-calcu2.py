def plus(op1, op2):
    if op1 == 0:
        return op2
    elif op2 == 0:
        return op1
    else:
        return plus(op1 + 1, op2 - 1)


def minus(op1, op2):
    if op2 == 0:
        return op1
    else:
        return minus(op1 - 1, op2 - 1)


def mal(op1, op2):
    if op1 == 0 or op2 == 0:
        return 0
    else:
        return plus(mal(op1, minus(op2, 1)), op1)


def teilen(op1, op2):
    if op2 == 0:
        return -1
    elif op1 < op2:
        return 0
    else:
        return plus(teilen(minus(op1, op2), op2), 1)


def modulo(op1, op2):
    if op2 == 0:
        return -1
    elif op1 < op2:
        return op1
    else:
        return modulo(minus(op1, op2), op2)


def potenz(op1, op2):
    if op2 == 0:
        return 1
    else:
        return mal(potenz(op1, minus(op2, 1)), op1)


def ggT(op1, op2):
    if op1 == 0:
        return op2
    elif op2 == 0:
        return op1
    else:
        return ggT(op2, modulo(op1, op2))


def min(op1, op2):
    if op1 == 0 or op2 == 0:
        return 0
    else:
        return plus(min(minus(op1, 1), minus(op2, 1)), 1)


def max(op1, op2):
    if op1 == 0:
        return op2
    elif op2 == 0:
        return op1
    else:
        return plus(max(minus(op1, 1), minus(op2, 1)), 1)


op1 = int(input("Wie lautet der erste Operand: "))
op2 = int(input("Wie lautet der zweite Operand: "))
op = input("Wie lautet der Operator: ")
if op == "+":
    print("Das Ergebnis lautet: {}".format(plus(op1, op2)))
elif op == "-":
    print("Das Ergebnis lautet: {}".format(minus(op1, op2)))
elif op == "*":
    print("Das Ergebnis lautet: {}".format(mal(op1, op2)))
elif op == "/":
    print("Das Ergebnis lautet: {}".format(teilen(op1, op2)))
elif op == "%":
    print("Das Ergebnis lautet: {}".format(modulo(op1, op2)))
elif op == "^":
    print("Das Ergebnis lautet: {}".format(potenz(op1, op2)))
elif op == "T":
    print("Das Ergebnis lautet: {}".format(ggT(op1, op2)))
elif op == "_":
    print("Das Ergebnis lautet: {}".format(min(op1, op2)))
elif op == "|":
    print("Das Ergebnis lautet: {}".format(max(op1, op2)))
else:
    print("Keine gültige Eingabe!")
