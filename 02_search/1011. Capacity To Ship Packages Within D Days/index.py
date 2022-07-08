"""https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
"""

# Approach 1


class Solution1:
    def shipWithinDays(self, weights, days):
        # tw: total weight
        tw = sum(weights)
        return self.find_min_weight(weights, days, tw)

    def find_min_weight(self, weights, days, total_weight):
        # 貨物全載
        if days == 1:
            return total_weight

        # mw: min weight
        left, mw = (0, None)
        for i, weight in enumerate(weights):
            # nw: next weights
            nw = weights[i+1:]
            # 下一回合限制天數大於貨物數量，直接 break
            if len(nw) < days-1:
                break

            # 已上船
            left += weight

            # cw: current weight
            cw = max(left, self.find_min_weight(nw, days-1, total_weight-left))
            mw = min(mw, cw) if mw else cw
        return mw

# Approach 2


class Solution2:
    def shipWithinDays(self, weights, days):

        def is_capable(weights, days, capacity):
            curr_weight = 0
            for w in weights:
                # 如果新貨物上船卻超載，則讓船開出去，減 1 天，新貨物上新船
                if curr_weight + w > capacity:
                    days -= 1
                    curr_weight = w
                else:
                    curr_weight += w
            # 全部跑完後，最少還要 1 天載剩下的
            return True if days > 0 else False

        max_weight = max(weights)
        total_weight = sum(weights)

        for capacity in range(max_weight, total_weight+1):
            if is_capable(weights, days, capacity):
                return capacity

# Approach 3


class Solution3:
    def shipWithinDays(self, weights, days):

        def is_capable(weights, limit_days, capacity):
            days = 1
            curr_weight = 0
            for w in weights:
                if curr_weight + w > capacity:
                    days += 1
                    if days > limit_days:
                        return False
                    curr_weight = 0
                curr_weight += w
            return True

        max_weight = max(weights)
        total_weight = sum(weights)

        for capacity in range(max_weight, total_weight+1):
            if is_capable(weights, days, capacity):
                return capacity

# Approach 4


class Solution4:
    def shipWithinDays(self, weights, days):

        def is_capable(weights, limit_days, capacity):
            days = 1
            curr_weight = 0
            for w in weights:
                if curr_weight + w > capacity:
                    days += 1
                    if days > limit_days:
                        return False
                    curr_weight = 0
                curr_weight += w
            return True

        left, right = max(weights), sum(weights)

        while left < right:
            mid = (left + right) // 2
            if is_capable(weights, days, mid):
                right = mid
            else:
                left = mid + 1
        return left
