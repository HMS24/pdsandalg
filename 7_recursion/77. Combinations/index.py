"""https://leetcode.com/problems/combinations/
"""

# Approach 1 backtracking
"""
時間複雜度: 
    1. 最準確: C(n, 0)+C(n, 1)+C(n, k)
    2. 相對準確: kC(n, k)
                C(n, k) 組合結果
                k 為決策樹的高度
    3. 上限: kn^k
            n 為決策樹的選擇
            k 為決策樹的高度
            再乘上 k 為 code 當中要 copy k 個元素 append 進 results
空間複雜度:
    不算 results 的話 k
    因為 curr 要存 k 個元素
"""

class Solution_1:
    def combine(self, n, k):
        results = []
        self.backtracking(1, n, k, [], results)
        return results

    def backtracking(self, first, n, k, curr, results):
        if len(curr) == k:
            results.append(curr[:])
            return
        for i in range(first, n+1):
            curr.append(i)
            self.backtracking(i+1, n, k, curr, results)
            curr.pop()
