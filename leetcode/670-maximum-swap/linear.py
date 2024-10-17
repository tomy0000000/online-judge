# Let n be the length of num
#
# Time: O(n)
# Space: O(1)

from collections import defaultdict, deque


class Solution:
    def maximumSwap(self, num: int) -> int:
        digit_indexes = defaultdict(deque)
        digits = []
        for i, d in enumerate(str(num)):
            d = int(d)
            digits.append(d)
            digit_indexes[d].append(i)
        digit_index_keys = sorted(digit_indexes.keys())

        index_ptr = len(digit_index_keys) - 1
        for i, d in enumerate(digits):
            if not digit_indexes[digit_index_keys[index_ptr]]:
                index_ptr -= 1
            match_digit = digit_index_keys[index_ptr]
            if d == match_digit:
                digit_indexes[match_digit].remove(i)
                continue
            match_index = digit_indexes[match_digit].pop()
            digits[i], digits[match_index] = digits[match_index], digits[i]
            break
        return int("".join(str(d) for d in digits))
