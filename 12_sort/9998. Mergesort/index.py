class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
Mergesort

"""


class Solution:
    """
    split
        - get_middle_node
        - left = mergeSort(head)
        - right = mergeSort(mid.next)
    merge
        - compare left right

    [time complexity](./assets/mergesort.jpg)
    """

    def mergeSort(self, head):
        '''
        :type head: ListNode
        :rtype: ListNode
        '''
        return self.split(head)

    def split(self, head):
        # base case
        if head is None or head.next is None:
            return head

        mid_node = self._get_middle_node(head)
        right_head = mid_node.next
        mid_node.next = None

        left = self.split(head)
        right = self.split(right_head)

        return self.merge(left, right)

    @staticmethod
    def _get_middle_node(head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, left, right):
        start = ListNode()
        head = start

        while left and right:
            if left.val < right.val:
                start.next = left
                left = left.next
            else:
                start.next = right
                right = right.next
            start = start.next

        start.next = left or right

        return head.next
