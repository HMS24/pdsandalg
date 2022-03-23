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
https://leetcode.com/problems/linked-list-cycle-ii/discuss/1701128/C%2B%2BJavaPython-Slow-and-Fast-oror-Image-Explanation-oror-Beginner-Friendly

Floyd Cycle Algorithm

* 點
    起點 s 
    循環進入點 e 
    slow 及 fast 交會點 x
* 距離
    s 到 e 的距離 H
    e 到 x 的距離 D
    一圈的距離 L
* 演算
    因為 fast 的速率是 slow 的 2 倍
    所以
    slow 走 H+D
    fast 走 2H+2D
    又
    fast 實際上走 H+D+nL
    所以
    2H+2D = H+D+nL
    => H = (L-D) + (n-1)L

1. 先找到 slow 及 fast 的交會點
2. 重複 1 直到 slow == fast 否則 None
3. 再從交會點及從 head 設另一個指針，繼續走, 因為H = (L-D) + (n-1)L
4. 新交會點就是循環進入點

"""

class Solution_2:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                break
        else:
            return None
        
        while head != slow:
            head, slow = head.next, slow.next

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
