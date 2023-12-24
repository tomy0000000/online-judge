# Let n be the number of words in s.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        for each in range(len(s.split())):
            ans += s.split()[each][::-1]
            if each != len(s.split()) - 1:
                ans += " "
        return ans
