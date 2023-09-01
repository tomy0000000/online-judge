class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current["EOW"] = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current:
                return False
            current = current[char]
        return "EOW" in current

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current:
                return False
            current = current[char]
        return True
