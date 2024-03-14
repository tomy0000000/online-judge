// Let n be the length of nums
// Time: O(n)
// Space: O(n)

package onlinejudge

func numSubarraysWithSum(nums []int, goal int) int {
	one_indexes := []int{-1}
	for index, value := range nums {
		if value == 1 {
			one_indexes = append(one_indexes, index)
		}
	}
	one_indexes = append(one_indexes, len(nums))

	comb := 0
	for left := 1; left < len(one_indexes)-goal; left++ {
		var new_comb int
		if goal == 0 {
			length := one_indexes[left] - one_indexes[left-1] - 1
			new_comb = (1 + length) * length / 2
		} else {
			right := left + goal - 1
			z_left := one_indexes[left] - one_indexes[left-1] - 1
			z_right := one_indexes[right+1] - one_indexes[right] - 1
			new_comb = (z_left + 1) * (z_right + 1)
		}
		comb += new_comb
	}
	return comb
}
