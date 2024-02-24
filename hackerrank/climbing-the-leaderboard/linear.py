#!/bin/python3

import os

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#


def climbingLeaderboard(ranked: list[int], player: list[int]) -> list[int]:
    ans = []
    ri, rk = 0, 1
    for pi in range(len(player) - 1, -1, -1):
        while ri < len(ranked) - 1 and ranked[ri] > player[pi]:
            if ranked[ri + 1] != ranked[ri]:
                rk += 1
            ri += 1
        if ri == len(ranked) - 1 and player[pi] < ranked[ri]:
            ans.append(rk + 1)
        else:
            ans.append(rk)
    return reversed(ans)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
