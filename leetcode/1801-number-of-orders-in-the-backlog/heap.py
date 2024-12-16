# Let n be the length of orders
#
# Time: O(n)
# Space: O(n)

from heapq import heappop, heappush


class Solution:
    def getNumberOfBacklogOrders(self, orders: list[list[int]]) -> int:
        buy_heap = []
        sell_heap = []
        for p, q, t in orders:
            while q:
                if t == 0:
                    if sell_heap and sell_heap[0][0] <= p:
                        sell_p, sell_q = heappop(sell_heap)
                        if sell_q <= q:
                            q -= sell_q
                        else:
                            heappush(sell_heap, (sell_p, sell_q - q))
                            break
                    else:
                        heappush(buy_heap, (-p, q))
                        break
                if t == 1:
                    if buy_heap and -buy_heap[0][0] >= p:
                        buy_p, buy_q = heappop(buy_heap)
                        if buy_q <= q:
                            q -= buy_q
                        else:
                            heappush(buy_heap, (buy_p, buy_q - q))
                            break
                    else:
                        heappush(sell_heap, (p, q))
                        break
        return (sum(q for _, q in buy_heap) + sum(q for _, q in sell_heap)) % (
            10**9 + 7
        )
