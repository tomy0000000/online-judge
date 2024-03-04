# Let n be the length of tokens
#
# Time: O(n log n)
# Space: O(n)

from collections import deque


class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        tokens = deque(sorted(tokens))
        score, maxi = 0, 0
        while tokens:
            while tokens and tokens[0] <= power:
                power -= tokens.popleft()
                score += 1
                maxi = max(maxi, score)
            if tokens and score:
                power += tokens.pop()
                score -= 1
            else:
                break

        return maxi
