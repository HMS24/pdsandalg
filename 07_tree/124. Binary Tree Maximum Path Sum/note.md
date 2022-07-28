## Approach 1

Recursion
focus on one node
什麼 state 你要操作？ max value
再來從基本 case 開始看:
1. 有可能經過 root
2. 在左邊或在右邊

初始想法為算左右 2 邊的 max，如果負數就取 0，
然後將鄰近三角的節點相加，與記下來的最大值相比。
最後因為要構成 path 僅會有單邊 node + root 
所以 return  root.val + max(left, right)

```python
class Solution1:
    def maxPathSum(self, root):
        # negative infinity
        max_result = float('-inf')

        def get_max(root):
            nonlocal max_result

            if root is None:
                return 0

            # 負數不用考慮，因此與 0 做比較。
            left_max = max(0, get_max(root.left))
            right_max = max(0, get_max(root.right))

            # 與之前存的 max result 比較
            curr_max_path_sum = left_max + root.val + right_max
            max_result = max(max_result, curr_max_path_sum)

            # 構成 path 為左右子樹其一 node 與 root
            return root.val + max(left_max, right_max)

        get_max(root)

        return max_result
```