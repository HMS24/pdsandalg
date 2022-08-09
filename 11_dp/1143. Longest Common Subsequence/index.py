"""https://leetcode.com/problems/longest-common-subsequence/
"""


class Solution1:
    """
    text1 = abc 
    text2 = adc
    最長共同子序列為 2, ac

    bottom up
    比較最後一個字母
    * 相同，代表找到一個 common sequence, 分解成子問題, 字串均刪除最後一個字母。
    * 不同，有兩個選擇, 兩個字串分別刪除最後一個字母, 找最大值也就是 best common sequence

    i.e.

        ""  a   b   c
    ""  0   0   0   0
    a   0   1   1   1
    d   0   1   1   1
    c   0   1   1   2

    m: text1 長度
    n: text2 長度
    time: O(mn)
    space: O(mn)
    
    另外注意如何 generate cache ... 會有 bug
    """
    def longestCommonSubsequence(self, text1, text2):
        n1 = len(text1)
        n2 = len(text2)
        # cause bug because object reference.. id(cache[0][2]) == id(cache[1][2])
        # cache = [[0] * (n1+1)] * (n2+1)
        cache = [[0 for _ in range(n1+1)] for _ in range(n2+1)]

        # x 是 row 為 text2 length
        for x in range(1, n2+1):
            for y in range(1, n1+1):
                if text1[y-1] == text2[x-1]:
                    cache[x][y] = 1 + cache[x-1][y-1]
                else:
                    cache[x][y] = max(cache[x-1][y], cache[x][y-1])
        return cache[-1][-1]

class Solution2:
    """
    Time Limit Exceeded

    top down 
    跟 solution 1 很像
    但以 recursion 實作沒有 cache
    相當直覺的暴力解
    """
    def longestCommonSubsequence(self, t1, t2):
        if not t1 or not t2:
            return 0
        if t1[-1] == t2[-1]:
            return 1 + self.longestCommonSubsequence(t1[:-1], t2[:-1])
        return max(self.longestCommonSubsequence(t1[:-1], t2), self.longestCommonSubsequence(t1, t2[:-1]))
