def f(num):
    if num in DictF:
        return DictF[num]
    for n in range(max(DictF)+1, num+1):
        DictF[n] = DictF[n-1]+n
    return DictF[num]

def g(num):
    if num in DictG:
        return DictG[num]
    for n in range(max(DictG)+1, num+1):
        DictG[n] = f(n)+DictG[n-1]
    return DictG[num]

global DictF
DictF = {1: 1}
global DictG
DictG = {1: 1}

while True:
    try:
        n = int(input())
        if n not in DictF:
            DictF[n] = f(n)
            DictG[n] = g(n)
        print(DictF[n], DictG[n])
    except:
        break
