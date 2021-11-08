"""https://leetcode.com/problems/valid-anagram/
"""


# Approach 1
"""
1. 計算字母出現頻率，用 dict 儲存
2. 相比是否相等
"""


class Solution_1:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1
        for char in t:
            if char not in s_dict:
                return False
            s_dict[char] = s_dict.get(char) - 1
        for value in s_dict.values():
            if value != 0:
                return False
        return True


"""
1. 排序後
2. 比較字母是否一樣
"""


class Solution_2:
    def isAnagram(self, s: str, t: str) -> bool:
        s_arr = [*s]
        t_arr = [*t]

        if len(s_arr) != len(t_arr):
            return False

        self.mergeSort(s_arr)
        self.mergeSort(t_arr)

        for i, char in enumerate(s_arr):
            if char != t_arr[i]:
                return False

        return True

    def mergeSort(self, arr):
        n = len(arr)
        if n == 1:
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
