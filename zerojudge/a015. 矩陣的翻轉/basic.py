while True:
    try:
        L = []
        Cred = input().split()
        for each in range(int(Cred[0])):
            Cur = input().split()
            for Writ in range(len(Cur)):
                L.append(Cur[Writ])
        for printRow in range(int(Cred[1])):
            for printNum in range(int(Cred[0])):
                if printNum == int(Cred[0])-1:
                    print (L[printRow + int(Cred[1])*printNum])
                else:
                    print (L[printRow + int(Cred[1])*printNum], end = " ")
    except:
        break