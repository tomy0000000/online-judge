package onlinejudge

import "sort"

type byStart [][]int

func (p byStart) Len() int           { return len(p) }
func (p byStart) Swap(i, j int)      { p[i], p[j] = p[j], p[i] }
func (p byStart) Less(i, j int) bool { return p[i][1] < p[j][1] }

func findMinArrowShots(points [][]int) int {
	sort.Sort(byStart(points))
	arrows := 1
	end := points[0][1]

	for _, balloon := range points {
		if balloon[0] > end {
			arrows++
			end = balloon[1]
		} else {
			if balloon[1] < end {
				end = balloon[1]
			}
		}
	}

	return arrows
}
