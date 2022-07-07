## Approach 1

一開始想到的是暴力解，去窮舉所有載貨的組合，取最小可行載貨數量。
主要將問題拆解成較小的問題，從 2 天開始嘗試，然後 3, 4, ...。
以3 天的為例，首先逐步固定貨物，剩下的貨物 2 天載完。
不過在第 12 筆測資發生Time Limit Exceeded

<div style="margin:30px 0px"><img src="./IMG_6645.JPG" alt="_note" width="50%" height="40%"/></div>

```python
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
```