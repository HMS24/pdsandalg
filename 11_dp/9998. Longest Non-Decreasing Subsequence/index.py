"""
Longest Non-Decreasing Subsequence


https://afteracademy.com/blog/longest-increasing-subsequence
"""


class Solution:
    """
    e.g. 
    nums:           20  30  30  20  19  90
    max lengths:    1   1   1   1   1   1

    以 nums[2] 30 為例
    把 30 當作 subsequence 最後一個 element
    從前往後詢問 可不可以與 30 串接起來(<= 30 non decreasing)
    
    - 20 ? 
        前面沒有就 count 他自己
            nums:           20  30  30  20  19  90
            max lengths:    1   1   1   1   1   1

    - 30 ? 
        - index = 0, 20
            20 < 30 可以串成 20, 30
            在 20 的時候 max lengths 為 1 加上本身 30 為 2
            2 比 max_lengths[1] 1 大 因此取代

            nums:           20  30  30  20  19  90
            max lengths:    1   2   1   1   1   1

    - 30 ? 
        - index = 0, 20
            20 < 30 可以串成 20, 30
            nums:           20  30  30  20  19  90
            max lengths:    1   2   2   1   1   1
        - index = 1, 30
            30 = 30 可以串成 20, 30, 30
            nums:           20  30  30  20  19  90
            max lengths:    1   2   3   1   1   1

    - 20 ? 
        - index = 0, 20
            20 = 20 可以串成 20, 20
            nums:           20  30  30  20  19  90
            max lengths:    1   2   2   2   1   1
        - index = 1, 30
            無法
            nums:           20  30  30  20  19  90
            max lengths:    1   2   2   2   1   1 
        - index = 2, 30
            無法
            nums:           20  30  30  20  19  90
            max lengths:    1   2   2   2   1   1 
    ...
    ...

    時間複雜度
        - i in range(1, n)
            sum(1, n-1)
        - j in range (0, i)
            sum(0, i-1) = (i-1)-0+1 = i
        - max()
            O(1)
    
        => sum(1, n-1) * i * 1 = (1+(n-1) * (n-1)/2) = 1/2n^2 - 1/2n
            O(n^2)
    空間複雜度
        cache length = O(n)
    """
    def length_of_lnds(self, nums):
        n = len(nums)
        max_length = [1] * n
        maximun_so_far = 1

        for i in range(1, n):
            for j in range(0, i):
                if nums[i] >= nums[j]:
                    max_length[i] = max(max_length[i], max_length[j]+1)

            maximun_so_far = max(maximun_so_far, max_length[i])

        return maximun_so_far
