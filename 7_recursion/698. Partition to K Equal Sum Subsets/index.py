"""https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
"""

# Approach 1 backtracking
"""
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/180014/Backtracking-x-2

時間複雜度: 

空間複雜度:

"""

class Solution_1:
    def canPartitionKSubsets(self, nums, k):
        nums = sorted(nums, reverse=True)
        if sum(nums) % k != 0:
            return False
        target = sum(nums) / k
        buckets = [0] * k
        return self.backtracking(buckets, nums, target)

    def backtracking(self, buckets, nums, target , next_index=0):
        if next_index == len(nums):
            for num in buckets:
                if num != target:
                    return False
            return True
        for i in range(len(buckets)):
            if buckets[i] + nums[next_index] <= target:
                buckets[i] += nums[next_index]
                if self.backtracking(buckets, nums, target, next_index+1):
                    return True
                buckets[i] -= nums[next_index]
        return False

# Approach 2 dfs
"""
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/146579/Easy-python-28-ms-beats-99.5

時間複雜度: 

空間複雜度:

"""
class Solution_1:
    def canPartitionKSubsets(self, nums, k):
        nums.sort(reverse=True) # Game Changer 1
        buck, kSum = [0] * k, sum(nums) // k
        def dfs(idx):
            if idx == len(nums): return len(set(buck)) == 1
            for i in range(k):
                buck[i] += nums[idx]
                if buck[i] <= kSum and dfs(idx + 1): return True
                buck[i] -= nums[idx]
                if buck[i] == 0: break # Game Changer 2
            return False
        return dfs(0)