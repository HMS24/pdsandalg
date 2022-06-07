"""https://leetcode.com/problems/first-bad-version/
"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# Approach 1 two-pointer
class Solution_1:
    def firstBadVersion(self, n):
        start = 1
        end = n
        while start <= end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                end = mid - 1
            else:
                start = mid + 1
        return start
