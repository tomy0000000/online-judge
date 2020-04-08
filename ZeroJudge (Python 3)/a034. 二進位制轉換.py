import sys
for input in sys.stdin:
    Num = int(input)
    List = []
    while Num != 0:
        List.append(Num % 2)
        Num = Num // 2
    List.reverse()
    for each in range(len(List)):
        List[each] = str(List[each])
    print ("".join(List))