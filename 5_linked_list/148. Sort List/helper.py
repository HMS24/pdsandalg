# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def create_list(nums):
    n = len(nums)
    num_list = [*map(ListNode, nums)]
    for i in range(n-1):
        num_list[i].next = num_list[i+1]
    return num_list[0]

def print_list(cur: ListNode):
    if cur:
        print(cur.val, " -> ", end='')
        print_list(cur.next)
    else:
        print("None")
