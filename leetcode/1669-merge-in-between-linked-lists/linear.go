// Let n be the length of list1 and list2 combined
//
// Time: O(n)
// Space: O(n)

package onlinejudge

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeInBetween(list1 *ListNode, a int, b int, list2 *ListNode) *ListNode {
	left := list1
	for i := 0; i < a-1; i++ {
		left = left.Next
	}

	right := left
	for i := 0; i < b-a+2; i++ {
		right = right.Next
	}

	left.Next = list2
	for left.Next != nil {
		left = left.Next
	}

	left.Next = right

	return list1
}
