def swap(id1, id2):
    ints[id1], ints[id2] = ints[id2], ints[id1]
    singleints[id1], singleints[id2] = singleints[id2], singleints[id1]

global ints
global singleints

while True:
    try:
        lenofs = int(input())
        ints = list(map(int, input().split()))
        singleints = list(map(lambda x:int(str(x)[-1:]), ints))
        
        for i in range(len(ints)-1):
            for j in range(len(ints)-1, i, -1):
                if singleints[j] < singleints[j-1]:
                    swap(j, j-1)
        
        for each in list(set(singleints)):
            if singleints.count(each) != 1:
                group = ints[singleints.index(each):singleints.index(each)+singleints.count(each)]
                group.sort(reverse=True)
                ints[singleints.index(each):singleints.index(each)+singleints.count(each)] = group
        
        print(" ".join(list(map(str, ints))))
    except:
        break
