import sys
for input in sys.stdin:
    k = input.split()
    for each in range(len(k)):
        k[each] = int(k[each])
    if (k[0]*2+k[1])%3 == 0:
        print("普通")
    elif (k[0]*2+k[1])%3 == 1:
        print("吉")
    elif (k[0]*2+k[1])%3 == 2:
        print("大吉")
