# Let n be the length of the longest version string.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        parsed_v1 = list(map(int, version1.split(".")))
        parsed_v2 = list(map(int, version2.split(".")))

        length = max(len(parsed_v1), len(parsed_v2))
        while len(parsed_v1) < length:
            parsed_v1.append(0)
        while len(parsed_v2) < length:
            parsed_v2.append(0)

        if parsed_v1 < parsed_v2:
            return -1
        if parsed_v1 > parsed_v2:
            return 1
        return 0
