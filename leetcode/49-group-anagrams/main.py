# Let n be the length of strs, s be the length of the longest string in strs.
#
# Time: O(n * s log s)
# Space: O(n * s)


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans_set = {}
        for s in strs:
            h = "".join(sorted(s))
            if h in ans_set:
                ans_set[h].append(s)
            else:
                ans_set[h] = [s]

        ans = [ans_set[s] for s in ans_set]
        return ans
