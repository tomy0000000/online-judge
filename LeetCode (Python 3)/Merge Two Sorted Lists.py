# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def load(l, nodes):
    if len(nodes) == 0:
        nodes = [ListNode(l.val)]
    else:
        nodes[-1].next = ListNode(l.val)
        nodes.append(nodes[-1].next)
    return nodes

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        nodes = []
        while l1 or l2:
            if l1 is None:
                print("load l2", l2.val)
                nodes = load(l2, nodes)
                l2 = l2.next
            elif l2 is None:
                print("load l1", l1.val)
                nodes = load(l1, nodes)
                l1 = l1.next
            elif l1.val < l2.val:
                print("load l1", l1.val)
                nodes = load(l1, nodes)
                l1 = l1.next
            else:
                print("load l2", l2.val)
                nodes = load(l2, nodes)
                l2 = l2.next
        return None if len(nodes) == 0 else nodes[0]
