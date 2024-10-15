# Let n be the length of s
#
# Time: O(n)
# Space: O(1)


class Solution:
    def minimumSteps(self, s: str) -> int:
        s = list(s)
        length = len(s)
        swap = 0
        try:
            ptr_zero = s.index("0", s.index("1"))
        except:
            return 0
        for i in range(length):
            if ptr_zero >= length:
                break
            if s[i] != "0":
                s[i], s[ptr_zero] = s[ptr_zero], s[i]
                swap += ptr_zero - i
                while ptr_zero < length and s[ptr_zero] == "1":
                    ptr_zero += 1
        return swap
