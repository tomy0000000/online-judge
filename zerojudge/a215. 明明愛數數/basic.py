while True:
    try:
        St, Mk = list(map(int, input().split()))
        total = St
        cnt = 1
        while True:
            if total > Mk:
                break
            St += 1
            total += St
            cnt += 1
        print(cnt)
    except:
        break
