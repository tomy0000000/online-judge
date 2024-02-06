# Let n be the length of strs, s be the length of the longest string in strs.
#
# Time: O(n * s log s)
# Space: O(n * s)

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans_set = defaultdict(list)
        for s in strs:
            ans_set["".join(sorted(s))].append(s)

        return [ans_set[s] for s in ans_set]
