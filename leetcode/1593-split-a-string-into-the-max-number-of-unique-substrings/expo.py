# Let n be the length of s
#
# Time: O(n * 2 ^ n)
# Space: O(n)


class Solution:
    def split_count(self, s: str, flags: list[bool]) -> int:
        split = set()
        buf = ""
        for c, flag in zip(s, flags):
            buf += c
            if flag:
                if buf in split:
                    return -1
                split.add(buf)
                buf = ""
        return len(split)

    def maxUniqueSplit(self, s: str) -> int:
        length = len(s)
        total_combs = 2**length
        maxi = 0
        for i in range(total_combs):
            padded_bin = f"{bin(i)[2:]:0>{length-1}}"
            flags = [b == "1" for b in list(padded_bin)] + [True]
            maxi = max(maxi, self.split_count(s, flags))
        return maxi
