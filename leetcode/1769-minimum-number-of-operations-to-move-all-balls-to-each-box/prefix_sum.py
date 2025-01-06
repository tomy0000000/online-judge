# Let n be the length of boxes
#
# Time: O(n)
# Space: O(1)


class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        total = 0
        moves = 0
        for i, b in enumerate(boxes):
            if b == "1":
                total += 1
                moves += i

        left_count = 0
        ans = []
        for b in boxes:
            if b == "1":
                left_count += 1
            ans.append(moves)
            moves += left_count
            moves -= total - left_count
        return ans
