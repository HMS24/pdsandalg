"""https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



# Approach 1 iteration
"""
1 curr 有 next ?
    * 有
        * curr.next.val == curr.val ?
            * 相等
                * curr 指向 curr.next 的 next
                * 繼續 1
            * 不相等
                * curr = curr.next
    * 沒有
        * return head!
"""

class Solution_1:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        curr = head
        while curr.next:
            if curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head



# Approach 2 recursion
"""
可以遞迴！
"""

class Solution_2:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass



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
