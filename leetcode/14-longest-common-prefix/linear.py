# Let n be the max length of one of the string in strs.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        index = 0
        shortest_len = len(min(strs, key=len))
        for index in range(shortest_len):
            c = strs[0][index]
            if any([s[index] != c for s in strs]):
                return strs[0][:index]
            index += 1

        return strs[0][:shortest_len]
