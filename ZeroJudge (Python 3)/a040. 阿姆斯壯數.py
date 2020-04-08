import sys
for input in sys.stdin:
    Ranging = input.split()
    Ranging[0] = int(Ranging[0])
    Ranging[1] = int(Ranging[1])
    Results = []
    for each in range(Ranging[0], Ranging[1]+1):
        Sum = 0
        converted = list(str(each))
        for each_char in converted:
            Sum += int(each_char)**len(converted)
        if Sum == each:
            Results.append(each)
    if len(Results) > 0:
        for each in range(len(Results)):
            if each != len(Results)-1:
                print (Results[each], end = " ")
            else:
                print (Results[each])
    else:
        print ("none")