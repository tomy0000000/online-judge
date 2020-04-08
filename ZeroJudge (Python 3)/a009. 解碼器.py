import sys
for input in sys.stdin:
    Char = [chr(i) for i in range(32, 127)]
    enCoded = list(input.replace("\r","").replace("\n",""))
    deCoded = []
    for each in enCoded:
        Index = Char.index(each)
        deCoded.append(Char[Index - 7])
    print ("".join(deCoded))