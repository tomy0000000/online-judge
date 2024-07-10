# Let n be the length of logs
#
# Time: O(n)
# Space: O(1)


class Solution:
    def minOperations(self, logs: list[str]) -> int:
        depth = 0
        for log in logs:
            if log == "../":
                depth = max(0, depth - 1)
            elif log == "./":
                continue
            else:
                depth += 1
        return depth
