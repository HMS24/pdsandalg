## Approach 1

Iteration

直覺想到沿著 next 直到最後，然後開始排序。把排好的 head 往前丟。而上一層的 head 則與下一層 return 排序好的 head 依序比較大小後插入。因此會有兩種狀況：
* 小於排序好的第一個 node，直接串接
* 在中間才找到，插入 node 會有兩個動作，需要記錄 prev。

```python
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
```

#### 時間複雜度
總共遞迴 n 次，每一次的 function 都要依序比較下一層 return 的 list，最壞情況每次都比到最後一個。因此為 $\mathcal{O}({n}^{2})$
#### 空間複雜度
每一層的 function 為 $\mathcal{O}(1)$，總共遞迴 n level，因此空間複雜度為遞迴深度，$\mathcal{O}(n)$

## Approach 2

就將值轉換成熟悉的 list，排序好再串成新的 list。
    
```python
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
```

#### 時間複雜度
max(3n, $n\log_{2}{n}$) = $\mathcal{O}(n\log{n})$
#### 空間複雜度
遞迴的深度為 n，每一次遞迴都有可能重新 copy 新的 list 並且組合 nums 回傳！為 $\mathcal{O}({n}^{2})$

## Approach 3

top-bottom merge sort。
分而治之，linked-list 也能使用 merge sort:

1. 看清輸入、輸出都是一個 `ListNode` 
2. 若長度只有 1 ，無法拆分不需排序，直接回傳結束。
3. 拆成左右兩個 List : `left` `right` 
    實作 `get_mid_node(head)` 
4. 左右兩個List  `head` `mid` 呼叫`merge_sort`自己來排序 ( 會得到兩個排序過後的 List )
5. 把兩個排序過後的 List 合併成一個 ListNode 並回傳
    實作 `merge_sorted_list(left, right)`
    
```python
class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        
        mid = self.get_mid_node(head)

        # 需要把 left 的尾巴切掉，否則會一直 recursion 
        next_head = mid.next
        mid.next = None

        left = self.sortList(head)
        right = self.sortList(next_head)

        return self.merge_sorted_list(left, right)

    def get_mid_node(self, head):
        if not head or not head.next:
            return head
        
        # 取得 mid 可以同時進行 ，使用 slow fast pointer
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
    
        return slow

    def merge_sorted_list(self, head1, head2):
        if not head1 or not head2:
            return head1 or head2
        
        small = head1
        big = head2
        if head1.val > head2.val:
            small = head2
            big = head1
        small.next = self.merge_sorted_list(small.next, big)

        return small
```

#### 時間複雜度
遞迴的次數會一直拆分為 `left` 及 `right` ，總共拆分了 $\log n$ levels，每一個 level 要 find_mid_node 及 merge 為 2n，因此該時間複雜度為 $\mathcal{O}(n\log n)$

<div style="margin:30px 0px"><img src="https://i.imgur.com/CpBVDaa.jpg" alt="_note" width="50%" height="40%"/></div>

#### 空間複雜度
Space Complexity: $\mathcal{O}(\log n)$ , where n is the number of nodes in linked list. Since the problem is recursive, we need additional space to store the recursive call stack. The maximum depth of the recursion tree is $\mathcal{O}(\log n)$
#### 備註
在時間複雜度方面，始終想不到 get_mid_node 及 merge 兩個加起來的時間複雜度，但其實他們都在 遞迴的同一個 level 為 $2n$ 並不是 ${n}^{2}$