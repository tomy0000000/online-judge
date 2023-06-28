for Run in range(6):
    if Run == 0:
        Shit = input()
    else:
        Str = input().split()
        for each in range(len(Str)):
            Str[each] = int(Str[each].replace("\n","").replace("\r",""))
        print (max(Str))