# Let n be the length of word


class WordDictionary:
    END: str = "\n"

    def __init__(self):
        self.tries = {}

    def addWord(self, word: str) -> None:
        # Time: O(n)
        # Space: O(n)
        current = self.tries
        for c in word:
            if c not in current:
                current[c] = {}
            current = current[c]
        current[self.END] = {}

    def search(self, word: str) -> bool:
        return WordDictionary.search_level(self.tries, word)

    @staticmethod
    def search_level(root: dict[str, dict], word: str) -> bool:
        # Time: O(n)
        # Space: O(1)
        if not word:
            return WordDictionary.END in root
        c = word[0]
        if c == ".":
            return any([WordDictionary.search_level(root[k], word[1:]) for k in root])
        if c not in root:
            return False
        return WordDictionary.search_level(root[c], word[1:])
