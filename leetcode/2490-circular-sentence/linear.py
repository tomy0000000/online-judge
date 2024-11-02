# Let n be the length of sentence
#
# Time: O(n)
# Space: O(1)


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        prev = sentence[-1]
        for word in sentence.split(" "):
            if prev != word[0]:
                return False

            prev = word[-1]
        return True
