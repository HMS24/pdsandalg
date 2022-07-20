"""https://leetcode.com/problems/sort-list/
"""

from helper import ListNode
# Approach 1 暴力


class Solution1:
    def sortList(self, head):
        if not head or not head.next:
            return head

        sorted_head = self.sortList(head.next)
        first = sorted_head

        prev = None
        while sorted_head:
            if head.val < sorted_head.val:
                break
            prev = sorted_head
            sorted_head = sorted_head.next

        if not prev:
            head.next = sorted_head
            return head
        prev.next = head
        head.next = sorted_head
        return first

# Approach 2 重組


class Solution2:
    def sortList(self, head):
        if not head or not head.next:
            return head

        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        nums = self.mergeSort(nums)
        nums = [*map(ListNode, nums)]

        for i in range(len(nums)-1):
            nums[i].next = nums[i+1]

        return nums[0]

    def mergeSort(self, nums):
        if len(nums) == 1:
            return nums

        n = len(nums)
        mid = n // 2

        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])

        i = 0
        j = 0
        n_left = len(left)
        n_right = len(right)

        for k in range(n):
            if i == n_left:
                # 直接 right 後面剩下的接過來，增加記憶體負擔
                nums = nums[:k] + right[j:]
                break
            elif j == n_right:
                nums = nums[:k] + left[i:]
                break
            elif left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
        return nums

# Approach 3 top-down merge sort


class Solution3:
    def sortList(self, head):
        if not head or not head.next:
            return head

        mid = self.getMidNode(head)

        # 需要把 left 的尾巴切掉，否則會一直 recursion
        next_head = mid.next
        mid.next = None

        left = self.sortList(head)
        right = self.sortList(next_head)

        return self.mergeTwoList(left, right)

    def getMidNode(self, head):
        if not head or not head.next:
            return head

        # 取得 mid 可以同時進行 ，使用 slow fast pointer
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def mergeTwoList(self, head1, head2):
        if not head1 or not head2:
            return head1 or head2

        small = head1
        big = head2
        if head1.val > head2.val:
            small = head2
            big = head1
        small.next = self.mergeTwoList(small.next, big)

        return small
