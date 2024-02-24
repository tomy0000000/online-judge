#!/bin/python3

import os

# Let n be the length of a and b
#
# Time: O(n)
# Space: O(1)


def compareTriplets(a, b):
    score_a = 0
    score_b = 0
    for each in range(len(a)):
        if a[each] > b[each]:
            score_a += 1
        elif b[each] > a[each]:
            score_b += 1
    return [score_a, score_b]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
