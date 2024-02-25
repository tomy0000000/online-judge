# Let v be n and e be the length of flights
#
# Time: O(v * e * k)
# Space: O(v + e)


from collections import defaultdict, deque
from math import inf


class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        price_mat = [[-1 for _ in range(n)] for _ in range(n)]
        for start, end, price in flights:
            price_mat[start][end] = price

        ans = inf
        queue = deque([(src, 0, k + 1)])
        mini = defaultdict(lambda: inf)
        while queue:
            here, spent, stop = queue.popleft()
            mini[here] = spent
            if here == dst:
                ans = min(ans, spent)
                continue
            if stop == 0:
                continue
            for next_stop, price in enumerate(price_mat[here]):
                if price == -1:
                    continue
                if spent + price > ans:
                    continue
                if mini[next_stop] < spent + price:
                    continue
                queue.append((next_stop, spent + price, stop - 1))

        return ans if ans != inf else -1
