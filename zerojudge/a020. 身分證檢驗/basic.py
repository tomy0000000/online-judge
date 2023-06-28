import sys
for input in sys.stdin:
    Inputs = input
    Check = 0
    Dict = {
        "A":10,
        "B":11,
        "C":12,
        "D":13,
        "E":14,
        "F":15,
        "G":16,
        "H":17,
        "I":34,
        "J":18,
        "K":19,
        "L":20,
        "M":21,
        "N":22,
        "O":35,
        "P":23,
        "Q":24,
        "U":25,
        "S":26,
        "T":27,
        "U":28,
        "V":29,
        "W":32,
        "X":30,
        "Y":31,
        "Z":33
    }
    for each in Dict:
        Inputs = Inputs.replace(str(each),str(Dict[each]))
    Inputs = list(Inputs)
    for each in range(9):
        Check += int(Inputs[each+1])*(9 - each)
    Check += int(Inputs[0])
    Check += int(Inputs[10])
    if Check % 10 == 0:
        print ("real")
    else:
        print ("fake")