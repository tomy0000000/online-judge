while True:
    try:
        while True:
            t = int(input())
            if t == 0:
                break
            else:
                for i in range(t):
                    if i%7 != 0 and i == t-1:
                        print(i)
                    elif i%7 != 0:
                        print(i, end=" ")
    except:
        break