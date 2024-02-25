#!/bin/python3

import os

# Let n be the length of candles
#
# Time: O(n)
# Space: O(1)


def birthdayCakeCandles(candles):
    tallest = max(candles)
    return candles.count(tallest)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + "\n")

    fptr.close()
