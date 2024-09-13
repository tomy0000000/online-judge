# Let n be the length of the arr and m be the length of the queries.
#
# Time: O(n + m)
# Space: O(n)


class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        prefix = [arr[0]]
        for n in arr[1:]:
            prefix.append(prefix[-1] ^ n)
        prefix.append(0)

        ans = []
        for start, end in queries:
            ans.append(prefix[end] ^ prefix[start - 1])
        return ans
