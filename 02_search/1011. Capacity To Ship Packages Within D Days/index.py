"""https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
"""

# Approach 1
# Time Limit Exceeded


class Solution1:
    def shipWithinDays(self, weights, days):
        # tw: total weight
        tw = sum(weights)
        return self.find_min_weight(weights, days, tw)

    def find_min_weight(self, weights, days, total_weight):
        if days == 1:
            return total_weight

        # mw: min weight
        left, mw = (0, None)
        for i, weight in enumerate(weights):
            # nw: next weights
            nw = weights[i+1:]
            if len(nw) < days-1:
                break

            left += weight

            # cw: current weight
            cw = max(left, self.find_min_weight(nw, days-1, total_weight-left))
            mw = min(mw, cw) if mw else cw
        return mw
