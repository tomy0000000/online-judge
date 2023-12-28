# Let n be the length of s
#
# Time: O(n ^ 2 * k)
# Space: O(n * k)


class Solution:
    def run_length_length(self, count: int) -> int:
        """Given a count, return the length of the compressed string

        E.g.
        0 -> 0 (no characters)
        1 -> 1 (c -> c)
        2 -> 2 (cc -> c2)
        3 -> 3 (ccc -> c3)

        Args:
            count (int): The count of the character

        Returns:
            int: The length of the compressed string
        """
        if count > 99:
            return 4
        if count > 9:
            return 3
        if count > 1:
            return 2
        return max(0, count)

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[n] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(0, k + 1):
                same, diff = 0, 0
                for l in range(i, 0, -1):
                    if s[l - 1] == s[i - 1]:
                        same += 1
                    else:
                        diff += 1

                    if j - diff >= 0:
                        dp[i][j] = min(
                            dp[i][j],
                            dp[l - 1][j - diff] + self.run_length_length(same),
                        )
                    else:
                        break

                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])

        return dp[n][k]
