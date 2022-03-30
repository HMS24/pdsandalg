"""https://leetcode.com/problems/add-two-numbers/
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



# Approach1 Iterative
"""
1. iterate l1 轉成 int
2. l2 同 1
3. 相加轉字串反轉
4. 建新的 node 串接
"""

class Solution_1:
    def addTwoNumbers(self, l1, l2):
        s1 = s2 = ""
        while l1:
            s1 = str(l1.val) + s1
            l1 = l1.next
        while l2:
            s2 = str(l2.val) + s2
            l2 = l2.next

        s = str(int(s1) + int(s2))[::-1]
        head = curr = ListNode()
        for num in s:
            curr.next = ListNode(int(num))
            curr = curr.next
        curr.next = None

        return head.next
        


# Approach2 Iterative
"""
1. 先加總串列對應元素值再加進位，並取商及餘數
2. 新串列串起餘數
3. 移動指標，重複 1 直到某串列為 None
4. 針對剩餘串列元素再做一次相加
5. 最後判斷有無進位在串起進位值

注意！！直接對 ListNode class 裡的 val 做修改不太好的做法
"""
class Solution_2:
    def addTwoNumbers(self, l1, l2):
        head = curr = ListNode()
        carry = 0

        while l1 and l2:
            sum = l1.val + l2.val + carry
            carry, remain = divmod(sum, 10)

            curr.next = ListNode(remain)
            curr = curr.next

            l1 = l1.next
            l2 = l2.next

        curr.next = l1 or l2
        while curr.next:
            sum = curr.next.val + carry
            carry, remain = divmod(sum, 10)

            curr.next.val = remain
            curr = curr.next

        if carry > 0:
            curr.next = ListNode(carry)

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
