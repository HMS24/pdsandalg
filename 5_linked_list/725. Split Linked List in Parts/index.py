"""https://leetcode.com/problems/split-linked-list-in-parts/
"""

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



# Approach1 Iterative
"""
"""

class Solution_1:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:   
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        q = length // k
        r = length % k
        group_counts = [q] * k
        for i in range(r):
            group_counts[i] += 1

        results = []
        for count in group_counts:
            results.append(head)
            prev = None

            while count:
                prev = head
                head = head.next
                count -= 1

            if prev:
                prev.next = None

        return results
 





























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
