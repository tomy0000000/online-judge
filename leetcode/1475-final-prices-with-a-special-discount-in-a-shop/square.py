# Let n be the length of prices
#
# Time: O(n ^ 2)
# Space: O(1)


class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        new_prices = []
        for i, p in enumerate(prices):
            for j in range(i + 1, len(prices)):
                pp = prices[j]
                if pp <= p:
                    p -= pp
                    break
            new_prices.append(p)
        return new_prices
