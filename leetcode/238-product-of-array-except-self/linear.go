// Let n be the length of nums
//
// Time: O(n)
// Space: O(n)

package onlinejudge

func productExceptSelf(nums []int) []int {
	zero_count := 0
	product := 1
	zero_product := 1

	for _, n := range nums {
		product *= n
		if n == 0 {
			zero_count++
		} else {
			zero_product *= n
		}
	}

	if zero_count >= 2 {
		return make([]int, len(nums))
	}

	results := []int{}
	for _, n := range nums {
		if n != 0 {
			results = append(results, product/n)
		} else {
			results = append(results, zero_product)
		}
	}

	return results
}
