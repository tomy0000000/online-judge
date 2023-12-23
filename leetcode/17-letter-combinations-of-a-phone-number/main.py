# Let n be the length of digits
#
# Time: O(n)
# Space: O(1)


class Solution:
    def build(self, exist: list[str], chars: list[str]) -> list[str]:
        return [f"{e}{c}" for e in exist for c in chars]

    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        keypad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        exist = list(keypad[digits[0]])
        for d in digits[1:]:
            exist = self.build(exist, keypad[d])
        return exist
