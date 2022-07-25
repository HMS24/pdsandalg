"""https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
"""

# Approach 1 backtracking


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

# Approach 2 backtracking


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
