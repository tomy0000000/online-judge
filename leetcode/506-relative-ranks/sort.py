# Let n be the length of score
#
# Time: O(n)
# Space: O(n)


class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        inter_ranks = sorted([(s, i) for i, s in enumerate(score)], reverse=True)
        ranks = score.copy()
        for rank, (_, ind) in enumerate(inter_ranks):
            rank += 1
            if rank == 1:
                ranks[ind] = "Gold Medal"
            elif rank == 2:
                ranks[ind] = "Silver Medal"
            elif rank == 3:
                ranks[ind] = "Bronze Medal"
            else:
                ranks[ind] = str(rank)
        return ranks
