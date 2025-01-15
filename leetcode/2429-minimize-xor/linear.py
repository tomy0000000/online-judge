# Let n be the length of num2
#
# Time: O(n)
# Space: O(n)


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bit_2 = list(bin(num2)[2:])
        bit_count_2 = bit_2.count("1")
        bit_1 = list(f"{bin(num1)[2:]:0>{len(bit_2)}}")
        bit_count_1 = bit_1.count("1")

        ptr = len(bit_1) - 1
        while bit_count_1 != bit_count_2:
            if bit_count_1 < bit_count_2:
                while bit_1[ptr] == "1":
                    ptr -= 1
                bit_1[ptr] = "1"
                bit_count_1 += 1
            else:
                while bit_1[ptr] == "0":
                    ptr -= 1
                bit_1[ptr] = "0"
                bit_count_1 -= 1
            ptr -= 1

        return int("".join(bit_1), base=2)
