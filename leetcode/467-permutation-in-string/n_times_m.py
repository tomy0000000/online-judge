# Let n be the length of s1 and m be the length of s2
#
# Time: O(n * m)
# Space: O(n)


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length = len(s1)

        # Get a dict of char count of s1
        s1_char_count = {char: s1.count(char) for char in s1}

        # Matching each substring
        for i in range(len(s2) - s1_length + 1):
            clone = s1_char_count.copy()
            sub_string = s2[i : i + s1_length]

            for c in sub_string:
                if c not in clone:
                    break
                if clone[c] == 0:
                    break
                clone[c] -= 1
            else:
                return True

        return False
