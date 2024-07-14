#!/bin/python3

# Let n be the length of w
#
# Time: O(n)
# Space: O(n)

import os
from bisect import bisect_right, insort


def biggerIsGreater(w):
    wl = list(w)
    chars = [w[-1]]
    for i in range(len(wl) - 2, -1, -1):
        if wl[i] < wl[i + 1]:
            next_char = chars[bisect_right(chars, wl[i])]
            chars.remove(next_char)
            insort(chars, wl[i])
            wl[i] = next_char
            wl[i + 1 :] = chars
            return "".join(wl)
        insort(chars, wl[i])
    return "no answer"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    T = int(input().strip())

    for T_itr in range(T):
        w = input()
        result = biggerIsGreater(w)
        fptr.write(result + "\n")

    fptr.close()
