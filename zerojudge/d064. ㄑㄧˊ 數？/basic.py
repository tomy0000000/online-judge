import sys
for input in sys.stdin:
    Num = int(input)
    if Num % 2 == 0:
        print ("Even")
    else:
        print ("Odd")