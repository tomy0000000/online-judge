# Let n be the length of sentence and m be the length of dictionary.
#
# Time: O(n * m)
# Space: O(1)


class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        dictionary.sort(key=len)
        new_sentence = []
        for word in sentence.split():
            for d in dictionary:
                if word.startswith(d):
                    new_sentence.append(d)
                    break
            else:
                new_sentence.append(word)
        return " ".join(new_sentence)
