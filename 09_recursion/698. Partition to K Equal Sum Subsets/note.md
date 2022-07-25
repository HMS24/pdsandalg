
## Approach 1

Backtracking

先把 nums 裡所有的數字先加總求出總和 sum，看看 sum 能不能被 k 整除，如果不能就直接返回 false。
如果可以被 k 整除，那麼接下來就可以用回溯法 (backtracking) 從第一個數字開始，由左到右放入桶子裡，
若此桶子已放不下則放入下個桶子裡；接著再放入第二個數字，依此類推，直到放完所有數字。
最後檢查筒子裡的數字是不是相等。

<div style="margin:30px 0px"><img src="https://i.imgur.com/0g7v4Va.jpg" alt="_note" width="40%" height="30%"/></div>

```python
class Solution1:
    def canPartitionKSubsets(self, nums, k):
        nums = sorted(nums, reverse=True)

        target = sum(nums) // k
        buckets = [0] * k

        # 判斷哪一個 bucket 要加上目前的元素 nums[index]
        def dfs(index):
            # 如果已經放進所有元素到 buckets 裡了，檢查是否 value 相等
            if index == len(nums):
                return len(set(buckets)) == 1

            # 對每一個 bucket
            for i in range(k):
                buckets[i] += nums[index]
                if buckets[i] <= target and dfs(index+1):
                    return True
                buckets[i] -= nums[index]

                # 將 nums[index] 放進 empty bucket[i]
                # 嘗試將 index 之後 的 num 放進來卻都失敗
                # 最後還把 nums[index] 移出 bucket
                # 代表 nums[index] 即使放新的 empty bucket 也不會得到解答，提前 break
                if buckets[i] == 0:
                    break

            return False

        return dfs(0)
```

## Approach 2

Backtracking

對每一個數字都試著放進桶子裡，如果符合 target 則桶子數 - 1。並且記錄已放過。
如果尚不符合 target 則往下繼續尋找 num。

```python
class Solution2:
    def canPartitionKSubsets(self, nums, k):
        # 沒有排序也可以，但有降冪排序的時候更快。因為再前幾個就能找到 curr_sum == target
        nums = sorted(nums, reverse=True)
        if sum(nums) % k != 0:
            return False
        target = sum(nums) / k
        visited = [False] * len(nums)

        def backtracking(k, start=0, curr_sum=0):
            if k == 1:
                return True
            if curr_sum > target:
                return False
            if curr_sum == target:
                return backtracking(k-1)
            for i in range(start, len(nums)):
                if not visited[i]:
                    visited[i] = True
                    if backtracking(k, i+1, curr_sum+nums[i]):
                        return True
                    visited[i] = False
            return False

        return backtracking(k)

```

* 時間複雜度
* 空間複雜度
* 思考
    從數字的角度思考
    
## 參考
* https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/180014/Backtracking-x-2