#!/bin/python3

# Let n be the length of arr
#
# Time: O(n * log(n))
# Space: O(1)


def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    total = len(arr)
    for n in arr:
        if n > 0:
            pos += 1
        elif n < 0:
            neg += 1
        else:
            zero += 1
    print(pos / total)
    print(neg / total)
    print(zero / total)


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
