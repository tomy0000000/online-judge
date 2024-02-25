#!/bin/python3

import os

# Let n be the length of c
#
# Time: O(n * log(n))
# Space: O(1)


def flatlandSpaceStations(n, c):
    c.sort()
    maxi = max(c[0], n - 1 - c[-1]) * 2
    for i in range(1, len(c)):
        distance = c[i] - c[i - 1]
        if not maxi or distance > maxi:
            maxi = distance
    if maxi == 1:
        return 0
    return maxi // 2


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + "\n")

    fptr.close()
