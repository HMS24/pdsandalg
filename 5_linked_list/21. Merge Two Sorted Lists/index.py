"""https://leetcode.com/problems/merge-two-sorted-lists/
"""

# Approach 1 Iteration
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

# Approach 2 Recursion
class Solution_2:
    def mergeTwoLists(self, list1, list2):
        if not list1 or not list2:
            return list1 or list2

        small_node = list1
        big_node = list2
        if list1.val > list2.val:
            small_node = list2
            big_node = list1

        small_node.next = self.mergeTwoLists(small_node.next, big_node)
        return small_node