while True:
    try:
        Letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        T = input()
        for each in range(len(T)-1):
            print(abs(Letters.find(T[each])-Letters.find(T[each+1])),end="")
        print()
    except:
        break