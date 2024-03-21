package onlinejudge

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	var prev *ListNode
	cur := head
	for cur != nil {
		cur.Next, cur, prev = prev, cur.Next, cur
	}
	return prev
}
