# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)


class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)

        ptr = -len(num_str)
        while ptr < -1 and num_str[ptr] == "9":
            ptr += 1
        replace_digit = num_str[ptr]
        maxi = int(num_str.replace(replace_digit, "9"))
        mini = int(num_str.replace(num_str[0], "0"))

        return maxi - mini
