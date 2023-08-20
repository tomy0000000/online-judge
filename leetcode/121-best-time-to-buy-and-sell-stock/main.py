# Let n be the length of prices.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        sell = None
        profs = []

        for p in prices:
            if p < buy:
                if sell:
                    profs.append(sell - buy)
                    sell = None
                buy = p
                continue
            if not sell or p > sell:
                sell = p

        if sell:
            profs.append(sell - buy)

        if not profs:
            return 0

        return max(profs)
