class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        for each in range(len(s.split())):
            ans += s.split()[each][::-1]
            if each != len(s.split())-1:
                ans += " "
        return ans
