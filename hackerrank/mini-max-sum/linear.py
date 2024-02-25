#!/bin/python3

# Let n be the length of arr
#
# Time: O(n)
# Space: O(1)


def miniMaxSum(arr):
    summ = sum(arr)
    mini = min(arr)
    maxi = max(arr)
    print(f"{summ-maxi} {summ-mini}")


if __name__ == "__main__":
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
