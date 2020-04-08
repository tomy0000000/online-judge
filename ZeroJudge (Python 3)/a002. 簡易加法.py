import sys
for s in sys.stdin:
    k = s.split()
    for each in range(len(k)):
        k[each] = int(k[each])
    print(sum(k))