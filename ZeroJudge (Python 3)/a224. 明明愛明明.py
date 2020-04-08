import re
while True:
    try:
        string = re.sub(r"[^a-z]*", "", input().lower())
        Dict = {}
        for c in string:
            if c in Dict:
                Dict[c] += 1
            else:
                Dict[c] = 1
        printed = False
        if len(string)%2 == 0:
            for k in Dict:
                if Dict[k]%2 != 0:
                    print("no...")
                    printed = True
                    break
            if not printed:
                print("yes !")
        else:
            single = False
            for k in Dict:
                if Dict[k]%2 != 0:
                    if single:
                        print("no...")
                        printed = True
                        break
                    else:
                        single = True
            if not printed:
                print("yes !")
    except:
        break
