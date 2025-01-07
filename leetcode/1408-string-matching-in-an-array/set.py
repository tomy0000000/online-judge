# Let n be the length of words
#
# Time: O(n ^ 2)
# Space: O(n)


class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        words.sort(key=len, reverse=True)
        previous = set()
        ans = []
        for word in words:
            for prev in previous:
                if word in prev:
                    ans.append(word)
                    break
            previous.add(word)
        return ans
