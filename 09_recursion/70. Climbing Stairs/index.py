"""https://leetcode.com/problems/climbing-stairs/
"""

# Recursion
class Solution1:
    def climbStairs(self, n):
        if n in (0, 1):
            return 1

        return self.climbStairs(n-1) + self.climbStairs(n-2)


# Dynamic top-down
class Solution2:
    def climbStairs(self, n):
        cache = [None] * (n+1)

        def climb(n):
            nonlocal cache

            if n in (0, 1):
                return 1

            if not cache[n]:
                cache[n] = climb(n-1) + climb(n-2)

            return cache[n]

        return climb(n)


# Dynamic bottom-up
class Solution3:
    def climbStairs(self, n):
        cache = [None] * (n+1)
        cache[0] = 1
        cache[1] = 1
        for i in range(2, n+1):
            cache[i] = cache[i-1] + cache[i-2]

        return cache[n]

# Dynamic bottom-up improve space
class Solution4:
    def climbStairs(self, n):
        # base case
        a = 1
        b = 1
        for _ in range(2, n+1):
            ways_num = a + b
            a, b = b, ways_num

        return b
