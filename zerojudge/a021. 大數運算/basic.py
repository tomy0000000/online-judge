import sys
for input in sys.stdin:
    Inputs = input.split()
    Inputs[0] = int(Inputs[0])
    Inputs[2] = int(Inputs[2])
    if Inputs[1] == "+":
        print (Inputs[0] + Inputs[2])
    elif Inputs[1] == "-":
        print (Inputs[0] - Inputs[2])
    elif Inputs[1] == "*":
        print (Inputs[0] * Inputs[2])
    elif Inputs[1] == "/":
        print (Inputs[0] // Inputs[2])