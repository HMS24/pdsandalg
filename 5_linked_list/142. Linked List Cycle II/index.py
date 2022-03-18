"""https://leetcode.com/problems/linked-list-cycle-ii/
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



# Approach1 Iterative
"""
ListNode{val: 1, 
    next: ListNode{val: 2, 
        next: ListNode{val: 3, 
            next: ListNode{val: 4, 
                next: ListNode{val: 5, 
                    next: None}}}}}

空間換取時間
利用 set 紀錄走過的 node 軌跡
"""

class Solution_1:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        if head is None:
            return head
        s = set()
        while head:
            if head in s:
                return head
            s.add(head)
            head = head.next
        return head



# Approach1 slow fast pointer
"""

"""

class Solution_2:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:        
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
