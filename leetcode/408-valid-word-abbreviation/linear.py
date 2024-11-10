# Let n be the length of word
#
# Time: O(n)
# Space: O(1)


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        abbr = list(abbr)
        i = 0
        while i < len(abbr) - 1:
            if abbr[i].isdigit() and abbr[i + 1].isdigit():
                abbr[i] = abbr[i] + abbr.pop(i + 1)
            else:
                i += 1

        ptr_word = 0
        ptr_abbr = 0
        while ptr_word < len(word) and ptr_abbr < len(abbr):
            if abbr[ptr_abbr].isdigit():
                if abbr[ptr_abbr].startswith("0"):
                    return False
                n = int(abbr[ptr_abbr])
                ptr_word += n
                ptr_abbr += 1
            else:
                if word[ptr_word] != abbr[ptr_abbr]:
                    return False
                ptr_word += 1
                ptr_abbr += 1

        if ptr_word != len(word) or ptr_abbr != len(abbr):
            return False

        return True
