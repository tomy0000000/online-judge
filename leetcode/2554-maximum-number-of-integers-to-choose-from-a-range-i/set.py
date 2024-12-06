# Time: O(n)
# Space: O(n)


class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        chosen = set()
        summ = 0
        for i in range(1, n + 1):
            if i in banned:
                continue

            if summ + i <= maxSum:
                chosen.add(i)
                summ += i
            else:
                break

        return len(chosen)
