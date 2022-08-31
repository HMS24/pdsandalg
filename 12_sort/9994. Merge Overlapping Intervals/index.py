"""
Merge Overlapping Intervals

Given a list of intervals A, return a new list with each overlapping intervals merged.

Note On Equivalent Boundaries: If an end-point and start-point of 2 intervals are equivalent (ex: [10, 11], [11, 12]) then the intervals also overlap.

Input: [[1, 5], [2, 3], [4, 10], [13, 15]]

|--|--|--|--|--|--|--|--|--|--|--|--|--|--|

x===========x
   x==x
         x=================x
                                    x=====x

Output: [[1, 10], [13, 15]]
Explanation: The first three intervals are merged into a single interval. The last interval cannot be merged since it is disjoint from the other intervals.
"""


class Solution1:
    """
    初始想法

    1. from mid split 2 sections
    2. until base case
        - len(A) == 1
    3. merge left and right
        - for loop len(A), compare 2 val, place smallest into position
            return [A[start], A[end]]
        - if left[start], left[end] < right[start] or \
            right[start], right[end] < left[end]
            return [left, right]
    4. recurse 1, 2, 3 step

    intervals 會重複 not an answer
    """

    def mergeOverlappingIntervals(self, A):
        if len(A) == 1:
            return A

        mid = len(A) // 2
        left = self.mergeOverlappingIntervals(A[:mid])
        right = self.mergeOverlappingIntervals(A[mid:])

        result = []
        for i in range(len(left)):
            for j in range(len(right)):
                list1, list2 = left[i], right[j]

                merged = self.merge(list1, list2)
                if len(merged) == 1:
                    right[j] = merged[0]
                    break
                result.append(list1)
        result.extend(right)

        return result

    def merge(self, list1, list2):
        if list1[0] < list2[0] and list1[1] < list2[0]:
            return [list1, list2]
        if list1[0] > list2[1] and list1[1] > list2[1]:
            return [list1, list2]

        smallest, biggest = list1[0], list1[1]
        for val in list2:
            smallest = min(smallest, val)
            biggest = max(biggest, val)

        return [[smallest, biggest]]


class Solution2:
    """
    - sorted by interval's start
        因為 兩個區間的 start 已經按非遞減方式排序
        所以要判斷是否 overlap 
        只要比較第二個區間的 start 是否被包含在第一個區間裡
        也就是 start <= 第一個區間的 end
    - 如果 overlap
        - merge 新的區間就是 [1_start, max(1_end, 2_end)]
        - 繼續往下比
    - 沒有 overlap
        - 1_interval append into result
        - 用 2_interval 繼續往下比

    time
        主要兩個 sort 跟 for iterate
        for iterate: O(n)
        sort: O(nlogn)
        O(nlogn)
    space
        sort 原地排序
        需要用 list records merged O(n)
    """

    def mergeOverlappingIntervals(self, A):
        if len(A) <= 1:
            return A

        A.sort(key=lambda x: x[0])

        merged_intervals = []
        curr_interval = A[0]

        for interval in A:
            start, end = interval

            if start <= curr_interval[1]:
                curr_interval[1] = max(curr_interval[1], end)
            else:
                merged_intervals.append(curr_interval)
                curr_interval = [start, end]

        merged_intervals.append(curr_interval)

        return merged_intervals
