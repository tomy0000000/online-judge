#!/bin/python3

# Time: O(n)
# Space: O(1)


def staircase(n):
    for i in range(1, n + 1):
        print((" " * (n - i)) + ("#" * i))


if __name__ == "__main__":
    n = int(input().strip())

    staircase(n)
