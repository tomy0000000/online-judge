# Time: O(1)
# Space: O(1)


class Solution:
    T = str.maketrans({"0": "1", "1": "0"})
    BIT_LENGTH = 12

    def add_one(self, bits: str) -> list[int]:
        bits = list(map(int, bits))
        i = len(bits) - 1
        while i >= 0 and bits[i] == 1:
            bits[i] = 0
            i -= 1
        else:
            if i == -1:
                bits.insert(0, 1)
            else:
                bits[i] = 1
        return bits

    def sub_one(self, bits: list[int]) -> str:
        i = len(bits) - 1
        while i >= 0 and bits[i] == 0:
            bits[i] = 1
            i -= 1
        else:
            if i == -1:
                bits.insert(0, 1)
            else:
                bits[i] = 0
        return "".join(map(str, bits))

    def to_two_comp(self, n: int) -> list[int]:
        bit_string = f"{bin(abs(n))[2:]:0>{self.BIT_LENGTH}}"
        if n > 0:
            return self.add_one(bit_string.translate(self.T))
        else:
            return list(map(int, bit_string))

    def from_two_comp(self, n: list[int]) -> int:
        if n[0] == 1:
            return int(self.sub_one(n).translate(self.T), 2)
        else:
            return -int("".join(map(str, n)), 2)

    def getSum(self, a: int, b: int) -> int:
        n1, n2 = self.to_two_comp(a), self.to_two_comp(b)
        carry = 0
        summ = []
        for d1, d2 in zip(n1[::-1], n2[::-1]):
            summ.append(d1 ^ d2 ^ carry)
            carry = (d1 & d2) | (d1 & carry) | (d2 & carry)
        return self.from_two_comp(summ[::-1])
