# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def readNode(n):
    tmp = [n.val]
    while n.next:
        n = n.next
        tmp.append(n.val)
    return tmp[::-1]

def rebuildNode(l):
    last = None
    for each in l:
        tmp = ListNode(each)
        if last:
            tmp.next = last
        last = tmp
    return last

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = int("".join([str(x) for x in readNode(l1)]))
        num2 = int("".join([str(x) for x in readNode(l2)]))
        return rebuildNode(list(str(num1+num2)))
