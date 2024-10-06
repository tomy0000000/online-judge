# Let n be the length of the longer sentence.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2:
            return True

        w1 = sentence1.split(" ")
        w2 = sentence2.split(" ")
        l1, l2 = len(w1), len(w2)
        min_length = min(l1, l2)

        front = 0
        while front < min_length and w1[front] == w2[front]:
            front += 1

        rear = 1
        while rear <= min_length and w1[l1 - rear] == w2[l2 - rear]:
            rear += 1
        rear -= 1

        return front + rear >= min_length
