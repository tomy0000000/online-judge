package onlinejudge

func findMaxLength(nums []int) int {
	prefix := []int{0}
	acc := 0
	for _, n := range nums {
		if n == 0 {
			acc++
		} else {
			acc--
		}
		prefix = append(prefix, acc)
	}

	locs := map[int][]int{}
	for i, p := range prefix {
		locs[p] = append(locs[p], i)
	}

	max := 0
	for _, loc := range locs {
		current := loc[len(loc)-1] - loc[0]
		if current > max {
			max = current
		}
	}
	return max
}
