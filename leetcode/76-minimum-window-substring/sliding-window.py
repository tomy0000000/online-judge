# Let n be the length of s
#
# Time: O(n)
# Space: O(1)


from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        tc = Counter(t)
        c = Counter()
        missing_chars = set(tc.keys())
        mini = ""

        while True:
            # Shift right
            if missing_chars and right < len(s):
                char = s[right]
                c[char] += 1
                right += 1

                # If this one is the missing char
                if char in missing_chars and c[char] >= tc[char]:
                    missing_chars.remove(char)

                # Let next iteration decide if shift right is done
                continue

            # Break if right bound reached end
            if missing_chars:
                break

            # New substring
            new_sub = s[left:right]
            mini = new_sub if not mini or len(new_sub) < len(mini) else mini

            # lefBreak if left bound reached end or minimum substring length found
            if left == len(s) - 1 or len(mini) == len(t):
                break

            # Shift left
            char = s[left]
            c[char] -= 1
            left += 1
            if c[char] < tc[char]:
                missing_chars.add(char)
            while s[left] not in tc:
                c[s[left]] -= 1
                left += 1

        return mini
