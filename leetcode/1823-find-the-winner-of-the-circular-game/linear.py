# Time: O(k)
# Space: O(n)


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(n))
        ptr = k - 1
        while len(friends) > 1:
            friends.pop(ptr)
            ptr = (ptr + k - 1) % len(friends)
        return friends[0] + 1
