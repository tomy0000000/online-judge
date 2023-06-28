while True:
    try:
        putin = input().split()
        if len(putin) == 1:
            Arr = input().split()
            for each in range(len(Arr)):
                Arr[each] = int(Arr[each])
            Arr.sort()
            print (*Arr)
    except:
        break