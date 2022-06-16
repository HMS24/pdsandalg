"""https://leetcode.com/problems/reverse-linked-list/
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



# Approach 1 錯誤
"""
沒有看清 input 以為是 node_list, [node, node]...

原題 input 輸入
ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}
"""

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



# Approach 2 Iterative / Swapping
"""
ListNode{val: 1, 
    next: ListNode{val: 2, 
        next: ListNode{val: 3, 
            next: ListNode{val: 4, 
                next: ListNode{val: 5, 
                    next: None}}}}}

1. head node 存在？ current = head
2. 存下 current.next
3. current.next 指向 prev=None
4. prev = current
5. current = next
"""

class Solution_2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        prev = None
        current = head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        return prev



# Approach 3 遞迴
"""
ListNode{val: 1, 
    next: ListNode{val: 2, 
        next: ListNode{val: 3, 
            next: ListNode{val: 4, 
                next: ListNode{val: 5, 
                    next: None}}}}}

1. 終止條件: 跑到 node(5), 也就是 next is None, 回傳 node(5)
2. 遞迴: 遞迴 node.next
3. 執行: node.next.next 指回自己(node)
4. 執行遞迴
5. 最後把 node(1) 指向 None
"""

class Solution_3:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:  
        if head is None:
            return head

        def recursion(head):
            if not head or head.next is None:
                return head

            tail = recursion(head.next)
            head.next.next = head
            return tail

        tail = recursion(head)
        head.next = None
        return tail



# Approach 4 遞迴優化
"""
ListNode{val: 1, 
    next: ListNode{val: 2, 
        next: ListNode{val: 3, 
            next: ListNode{val: 4, 
                next: ListNode{val: 5, 
                    next: None}}}}}

1. 終止條件: 跑到 node(5), 也就是 next is None, 回傳 node(5)
2. 遞迴: 遞迴 node.next
3. 執行: node.next.next 指回自己(node)
4. 執行: node.next 指向 None (下一輪的 prev 閉包已記住當時的 head node)!
5. 執行遞迴
"""

class Solution_4:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:  
        if not head or head.next is None:
            return head

        prev = head
        head = self.reverseList(prev.next)
        prev.next.next = prev
        prev.next = None
        return head



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
