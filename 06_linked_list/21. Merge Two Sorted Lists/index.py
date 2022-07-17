"""https://leetcode.com/problems/merge-two-sorted-lists/
"""

from helper import ListNode

# Approach 1 Iteration


class Solution1:
    def mergeTwoLists(self, list1, list2):
        head = curr = ListNode(0)

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = list1 or list2

        return head.next

# Approach 2 Recursion


class Solution2:
    def mergeTwoLists(self, list1, list2):
        if not list1 or not list2:
            return list1 or list2

        (small, big) = (list1, list2) if list1.val < list2.val else (list2, list1)
        small.next = self.mergeTwoLists(small.next, big)

        return small
