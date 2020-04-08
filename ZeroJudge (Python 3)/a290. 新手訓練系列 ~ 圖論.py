def scanArrivable(current, visited, arrivable, dest):
    if dest in arrivable[current]:
        return True
    if len(visited) == len(arrivable):
        return False
    for each in arrivable[current]:
        if each in visited:
            continue
        visited.append(each)
        if scanArrivable(each, visited, arrivable, dest):
            return True
    return False
while True:
    try:
        citiNum, roadNum = list(map(int, input().split()))
        arrivable = [[] for i in range(citiNum)]
        for rI in range(roadNum):
            fr, to = list(map(int, input().split()))
            arrivable[fr-1].append(to-1)
        
        exfr, exto = list(map(int, input().split()))
        exfr -= 1
        exto -= 1
        
        if exto in arrivable[exfr]:
            print("Yes!!!")
        elif scanArrivable(exfr, [exfr], arrivable, exto):
            print("Yes!!!")
        else:
            print("No!!!")
    except:
        break