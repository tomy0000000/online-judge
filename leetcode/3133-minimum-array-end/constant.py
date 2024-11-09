# Time: O(1)
# Space: O(1)


class Solution:
    def minEnd(self, n: int, x: int) -> int:
        x_bit = bin(x)[2:]
        x_bit_zeros = x_bit.count("0")
        group_size = 2**x_bit_zeros

        n -= 1
        ans_bits = list(x_bit)
        right_bits = bin(n % group_size)[2:]
        right_bits = f"{right_bits:0>{x_bit_zeros}}"
        ptr = 0
        for i, b in enumerate(ans_bits):
            if b == "1":
                continue
            ans_bits[i] = right_bits[ptr]
            ptr += 1

        ans_bits = "".join(ans_bits)

        left_bits = bin(n // group_size)[2:]
        if left_bits != "0":
            ans_bits = left_bits + ans_bits

        return int(ans_bits, base=2)
