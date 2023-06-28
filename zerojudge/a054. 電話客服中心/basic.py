import sys
for input in sys.stdin:
    Inputs = list(input)
    Check = 0
    for each in range(8):
        Check += int(Inputs[each])*(8 - each)
    Check += int(Inputs[8])
    Check = 10 - (Check % 10)
    if Check == 10:
        print ("BNZ")
    elif Check == 1:
        print ("AMW")
    elif Check == 2:
        print ("KLY")
    elif Check == 3:
        print ("JVX")
    elif Check == 4:
        print ("HU")
    elif Check == 5:
        print ("GT")
    elif Check == 6:
        print ("FS")
    elif Check == 7:
        print ("ER")
    elif Check == 8:
        print ("DOQ")
    elif Check == 9:
        print ("CIP")