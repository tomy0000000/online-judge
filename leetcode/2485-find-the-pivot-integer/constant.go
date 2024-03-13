// Time: O(1)
// Space: O(1)

package main

import "math"

func pivotInteger(n int) int {
	summ := (1 + n) * n / 2
	root := math.Sqrt(float64(summ))
	if float64(int(root)) == root {
		return int(root)
	}
	return -1
}
