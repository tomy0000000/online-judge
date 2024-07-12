# Let n be the length of s
#
# Time: O(n)
# Space: O(n)


class Solution:
    def process_token(self, s: str, token: str) -> tuple[str, int]:
        splits = 0
        while token in s:
            loc = s.find(token)
            s = s[:loc] + s[loc + len(token) :]
            splits += 1
        return s, splits

    def process_word(self, s: str, x: int, y: int) -> int:
        if x > y:
            s, p1 = self.process_token(s, "ab")
            s, p2 = self.process_token(s, "ba")
        else:
            s, p2 = self.process_token(s, "ba")
            s, p1 = self.process_token(s, "ab")
        return p1 * x + p2 * y

    def maximumGain(self, s: str, x: int, y: int) -> int:
        prev_ab = s[0] in ("a", "b")
        cuts = []
        if prev_ab:
            cuts.append(0)
        for i, c in enumerate(s):
            if c in ("a", "b"):
                if not prev_ab:
                    cuts.append(i)
                prev_ab = True
            else:
                if prev_ab:
                    cuts.append(i)
                prev_ab = False

        words = []
        for i in range(0, len(cuts), 2):
            begin = cuts[i]
            end = cuts[i + 1] if i + 1 < len(cuts) else len(s)
            word = s[begin:end]
            words.append(word)

        return sum(self.process_word(word, x, y) for word in words)
