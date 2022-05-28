"""https://leetcode.com/problems/sort-list/
"""

# n^2
# n
# Approach 1 Recursion
class Solution_1:
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

# nlogn
# n
# Approach 2 Recursion imporoved
class Solution_2:
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
