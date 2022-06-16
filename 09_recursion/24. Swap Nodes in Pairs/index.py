"""https://leetcode.com/problems/swap-nodes-in-pairs/
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



# Approach 1 recursion
"""
"""

class Solution_1:
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        next = head.next
        next_pair_head = head.next.next
        head.next.next = head
        head.next = self.swapPairs(next_pair_head)
        return next



# Approach 2 iteration
"""
"""

class Solution_2:
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head

        next = head.next

        while head and head.next:
            next_pair_head = head.next.next
            head.next.next = head
            if next_pair_head is None or next_pair_head.next is None:
                head.next = next_pair_head
            else:
                head.next = next_pair_head.next
            head = next_pair_head
        return next


""" HELP
印出 ListNodes
"""
class ListNode:
    def __init__(self, val):
        self.next = None
        self.val = val

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e

def printList(cur: ListNode):
    if cur:
        print(cur.val, " -> ", end='')
        printList(cur.next)
    else:
        print("None")
        
printList(a)
