# Let n be the length of position
#
# Time: O(n log n)
# Space: O(1)


class Solution:
    def possible(self, position: list[int], m: int, force: int) -> bool:
        last_pos_ind = 0
        ind = 1
        pos_len = len(position)
        m -= 1
        while m and ind < pos_len:
            if position[ind] - position[last_pos_ind] >= force:
                m -= 1
                last_pos_ind = ind
            else:
                ind += 1
        return m == 0

    def maxDistance(self, position: list[int], m: int) -> int:
        position.sort()
        left = 1
        right = (position[-1] - position[0]) // (m - 1) + 1

        while left < right:
            mid = (left + right) // 2
            if self.possible(position, m, mid):
                left = mid + 1
            else:
                right = mid
        return left if self.possible(position, m, left) else left - 1
