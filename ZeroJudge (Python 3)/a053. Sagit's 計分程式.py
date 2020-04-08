import sys
for input in sys.stdin:
    Inputs = int(input)
    if Inputs <= 10:
        print (Inputs*6)
    elif Inputs >= 11 and Inputs <= 20:
        print (60 + (Inputs-10)*2)
    elif Inputs >= 21 and Inputs <= 40:
        print (80 + (Inputs-20)*1)
    elif Inputs >= 40:
        print (100)