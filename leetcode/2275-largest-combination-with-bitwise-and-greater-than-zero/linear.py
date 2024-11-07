# Let n be the length of candidates
#
# Time: O(n)
# Space: O(n)


class Solution:
    def largestCombination(self, candidates: list[int]) -> int:
        bin_length = 0
        bins = []
        for n in candidates:
            n_bin = bin(n)[2:]
            bins.append(n_bin)
            bin_length = max(bin_length, len(n_bin))

        for i, n_bin in enumerate(bins):
            bins[i] = f"{n_bin:0>{bin_length}}"

        return max(
            sum(int(n_bin[i] == "1") for n_bin in bins) for i in range(bin_length)
        )
