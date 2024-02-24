#!/bin/python3

import os

# Let n be the numer of cells in the matrix
#
# Time: O(n)
# Space: O(1)


def diagonalDifference(arr):
    n = len(arr)
    primary = sum([arr[i][i] for i in range(n)])
    secondary = sum([arr[i][n - i - 1] for i in range(n)])
    return abs(primary - secondary)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + "\n")

    fptr.close()
