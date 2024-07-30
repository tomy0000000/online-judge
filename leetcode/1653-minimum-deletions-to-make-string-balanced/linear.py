# Let n be the length of s
#
# Time: O(n)
# Space: O(n)


class Solution:
    def minimumDeletions(self, s: str) -> int:
        length = len(s)

        left_b = [0 for _ in range(length)]
        b_count = 0
        for i in range(length):
            left_b[i] = b_count
            if s[i] == "b":
                b_count += 1

        right_a = [0 for _ in range(length)]
        a_count = 0
        for i in range(length - 1, -1, -1):
            right_a[i] = a_count
            if s[i] == "a":
                a_count += 1

        return min(left_b[i] + right_a[i] for i in range(length))
