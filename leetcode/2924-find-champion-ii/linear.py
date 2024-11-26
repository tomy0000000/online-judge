# Let n be the length of edges
#
# Time: O(n)
# Space: O(n)


class Solution:
    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        if not edges:
            return 0 if n == 1 else -1

        winners = set()
        losers = set()
        for winner, loser in edges:
            losers.add(loser)
            if loser in winners:
                winners.remove(loser)

            if winner not in losers and winner not in winners:
                winners.add(winner)

        if len(winners) + len(losers) < n:
            return -1

        return winners.pop() if len(winners) == 1 else -1
