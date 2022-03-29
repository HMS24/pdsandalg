"""https://leetcode.com/problems/merge-two-sorted-lists/
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



# Approach1 Iterative
"""
新增 listnode 當指標
比較兩個 listnode  的 val
指標的 next 串接較小的..
"""

class Solution_1:
    def mergeTwoLists(self, list1, list2):
        head = ptr = ListNode(0)

        while list1 and list2:
            if list1.val < list2.val:
                ptr.next = list1
                list1 = list1.next
            else:
                ptr.next = list2
                list2 = list2.next
            ptr = ptr.next
        ptr.next = list1 or list2

        return head.next    
        


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
