# Let n be the length of words and m be the length of queries.
#
# Time: O(n + m)
# Space: O(n)


class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        vowels = {"a", "e", "i", "o", "u"}
        valids = [word[0] in vowels and word[-1] in vowels for word in words]
        prefix = [0]
        for valid in valids:
            prefix.append(prefix[-1] + int(valid))
        return [prefix[e + 1] - prefix[s] for s, e in queries]
