"""https://leetcode.com/problems/group-anagrams/
"""


# Approach 1
"""
1. 對每個 word 排序當作 dict 的 key
2. 對每個 dict 的 key value append word
"""


class Solution_1:
    def groupAnagrams(self, strs):
        d = {}
        for w in strs:
            w_list = [*w]
            self.mergeSort(w_list)
            key = (*w_list, )
            d[key] = d.get(key, []) + [w]

        return d.values()

    def mergeSort(self, arr):
        n = len(arr)
        if n <= 1:
            return

        mid = n // 2
        left = arr[0:mid]
        right = arr[mid:n]

        self.mergeSort(left)
        self.mergeSort(right)

        i = 0
        j = 0
        for index in range(n):
            if i == len(left):
                arr[index] = right[j]
                j += 1
            elif j == len(right):
                arr[index] = left[i]
                i += 1
            elif left[i] <= right[j]:
                arr[index] = left[i]
                i += 1
            else:
                arr[index] = right[j]
                j += 1

        return
