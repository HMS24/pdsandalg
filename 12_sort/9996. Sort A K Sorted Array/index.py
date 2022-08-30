"""
Sort A K Sorted Nums

Given a "k sorted Nums" return the fully sorted version of the sequence.

A "k sorted Nums" is a sequence whose elements are no more than k positions left or right from their position in the fully sorted sequence.

Input: 
k = 2
[3, 4, 1, 2, 5]

Distances from final sorted position:
1: 2 positions right
2: 2 positions right
3: 2 positions left
4: 2 positions left
5: 0 positions away

Output: [1, 2, 3, 4, 5]
"""

import heapq

class Solution:
    def sortNearlySortednums(self, nums, k):
        """
        :type nums: list of int
        :type k: int
        :rtype: list of int

        - build min heap with k+1 elem
        - pop min heap and place to `0 index`(placement_pointer)
        - push `k+2`(next_read_pointer) elem into min heap
        - iterate above steps until next_read_pointer >= n
        - pop min heap rest elem and place

        e.g. 
        k = 2
        3   4   1   2   5

        相對應的可以放的位置
        3   3   3
        4   4   4   4
        1   1   1   1   1
            2   2   2   2
                5   5   5
        
        而對 index 0 來說
        3, 4, 1 坐在這個位置？
        明顯是最小的 1
        
        What data structure helps me with keeping track of minimums and maximums in a set of data very well?
        A Heap.

        找 smallest or biggest can use Heap structure
        放完 1 之後
        第二輪
        3, 4, 2 誰可以坐在 index 1 的位置？
        2..
        ...
        ...
        ...

        time complexity
            對 n 個 elem 來說
            每個 elem 都需要 push into heap 去 compare => worst case compare all levels => logk
            O(n*logk)
        space complexity
            要 maintain 一個 min heap hold k+1 nums
            O(k)
        """
        # Creating a minimum priority queue
        min_heap = []
        n = len(nums)
        
        for i in range(k+1):
            if i >= n:
                break
            
            heapq.heappush(min_heap, nums[i])

        placement_pointer = 0
        next_read_pointer = k + 1

        while next_read_pointer < n:
            nums[placement_pointer] = heapq.heappop(min_heap)
            placement_pointer += 1

            heapq.heappush(min_heap, nums[next_read_pointer])
            next_read_pointer += 1

        # 剩下的直接相對應的位置就好
        while placement_pointer < n:
            nums[placement_pointer] = heapq.heappop(min_heap)
            placement_pointer += 1
        
        return nums
