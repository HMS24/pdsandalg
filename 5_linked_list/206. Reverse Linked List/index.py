"""https://leetcode.com/problems/reverse-linked-list/
"""
from typing import Optional

# Approach 1 錯誤
"""
沒有看清 input 以為是 node_list, [node, node]...

原題 input 輸入
ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution_1:
    """錯誤解法"""
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        for i, cur_n in enumerate(head):
            if i == len(head)-1:
                return
            if i == 0:
                cur_n.next = None
            
            next_n = head[i+1]
            next_n.next = cur_n

        return head