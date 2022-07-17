## Approach 1

Iteration

新增一個 virtual Node 當指標 curr。
如果兩邊都有節點，則重複比較兩節點的大小，取較小的串接在 virtual Node 後面。
直到僅剩單邊或者兩邊均無，通通串在最後面。

```python
class Solution1:
    def mergeTwoLists(self, list1, list2):
        head = curr = ListNode(0)

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = list1 or list2

        return head.next
```

#### 時間複雜度
最壞情況下，兩邊長度(m, n)相等且比較值的大小之後屬於交叉串接，那麼時間複雜度為 O($2{n}$) = O(${n}$)
#### 空間複雜度
需要多新增一個 Virtual Node 其餘均為常數，O(${1}$)

## Approach 2

* 比較 2 個 node 的 val 誰比較小，取小的 node。
* 將剛才較大的 node 繼續與剛才值較小的 node 的 next 比較。
* 直到比完，若還有剩則直接串接在後面。
    
```python
class Solution2:
    def mergeTwoLists(self, list1, list2):
        if not list1 or not list2:
            return list1 or list2

        (small, big) = (list1, list2) if list1.val < list2.val else (list2, list1)
        small.next = self.mergeTwoLists(small.next, big)

        return small
```

#### 時間複雜度
最差情況也是交叉串連，不斷往下遞迴直到 None，其時間複雜度為 O(${n}$)。
#### 空間複雜度
最差情況往下遞迴的深度為 2n ，空間複雜度為 O(${n}$)
