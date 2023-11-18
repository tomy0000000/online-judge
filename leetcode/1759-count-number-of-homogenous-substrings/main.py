# Let n be the length of s.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def countHomogenous(self, s: str) -> int:
        div = 1000000000 + 7
        acc = 0
        cur = ""
        answer = 0
        for c in s:
            answer += 1
            if c == cur:
                acc += 1
                answer += acc
            else:
                acc = 0
                cur = c
        return answer % div
