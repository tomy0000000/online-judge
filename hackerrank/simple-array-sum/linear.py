#!/bin/python3

# Let n be the length of ar
#
# Time: O(n)
# Space: O(1)


import os


def simpleArraySum(ar):
    return sum(ar)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + "\n")

    fptr.close()
