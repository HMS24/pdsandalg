"""https://leetcode.com/problems/edit-distance/
"""


class Solution1:
    """
    recursion
    """

    def minDistance(self, s1, s2):
        def dfs(i, j):
            if i == len(s1):
                return len(s2) - j
            if j == len(s2):
                return len(s1) - i
            if s1[i] == s2[j]:
                return dfs(i+1, j+1)

            insert = dfs(i, j+1)
            replace = dfs(i+1, j+1)
            delete = dfs(i+1, j)

            return 1 + min(insert, replace, delete)

        return dfs(0, 0)


class Solution2:
    """
    bottom-up
    """

    def minDistance(self, s1, s2):
        m = len(s1)
        n = len(s2)

        dp = [[0] * (m+1) for _ in range(n+1)]

        for i in range(1, m+1):
            dp[0][i] = i

        for j in range(1, n+1):
            dp[j][0] = j

        for x in range(1, n+1):
            for y in range(1, m+1):
                if s1[y-1] == s2[x-1]:
                    dp[x][y] = dp[x-1][y-1]
                    continue

                insert = dp[x-1][y] + 1
                replace = dp[x-1][y-1] + 1
                delete = dp[x][y-1] + 1

                dp[x][y] = min(insert, replace, delete)

        return dp[-1][-1]
