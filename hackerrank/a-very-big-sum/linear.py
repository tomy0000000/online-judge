#!/bin/python3

import os

# Let n be the length of ar
#
# Time: O(n)
# Space: O(1)


def aVeryBigSum(ar):
    return sum(ar)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + "\n")

    fptr.close()
