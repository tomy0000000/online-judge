# Let n be the length of citations
#
# Time: O(n * log n)
# Space: O(1)


class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        for i, p in enumerate(citations):
            if p < i + 1:
                return i
        return len(citations)
