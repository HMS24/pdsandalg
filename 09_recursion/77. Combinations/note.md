## Approach 1

組合公式

從 m 個數中取出 n 個數之公式解為 $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$
因此每次取出數字時分為兩種情況:

* 必取第一個數字，還需在其餘數字中取出 k - 1 個數字
* 不取第一個數字，需在剩餘的數字中取出 k 個數字，每取出一個數字就依次遞減

```python
class Solution2:
    def combine(self, n, k):
        # e.g. c(4, 1) = [[1], [2], [3], [4]]
        if k == 1:
            return [[i] for i in range(1, n+1)]
         # e.g. c(4, 4) = [[1, 2, 3, 4]]
        if k == n:
            return [[*range(1, n+1)]]

        results1 = self.combine(n-1, k-1)
        # 一定要取第 1 個數字也就是 n
        results1 = [item+[n] for item in results1]

        results2 = self.combine(n-1, k)
        return results1 + results2
```

#### 時間複雜度
最壞情況每次 n 都會分 2 組遞迴，$\mathcal{O}({2}^{n})$
#### 空間複雜度
function call stack 為樹的高度 $\mathcal{O}({k})$

## Approach 2

backtracking

取第一個數字，然後從剩餘的 N - 1 個數字中取出其中一個，再從剩餘的 N - 2 個數字中取出其中一個，直到取出 k 個數字；下一輪則先取出第二個數字，再從後面的 N - 2 個數字中取出其中一個，這樣循環下去，直到找出所有組合。

以 combine(4, 2) 為例:

<div style="margin:30px 0px"><img src="https://i.imgur.com/erLQ8h9.png" alt="_note" width="50%" height="40%"/></div>

```python
class Solution1:
    def combine(self, n, k):
        results = []

        def backtracking(start, curr):
            if len(curr) == k:
                return results.append(curr[:])
            for i in range(start, n+1):
                curr.append(i)
                backtracking(i+1, curr)
                curr.pop()

        backtracking(1, [])

        return results
```

#### 時間複雜度:
* 最準確: 
    $\mathcal{O}(\sum\limits_{x = 0}^k {\binom{n}{x}})$
* 相對準確: 
    $\mathcal{O}(k \binom{n}{k})$，$\binom{n}{k}$ 為組合結果，k 為決策樹的高度。
* 上限: 
    $\mathcal{O}(k {n}^{k})$，n 為決策樹的選擇，k 為決策樹的高度。再乘上 k 為 code 當中要 copy k 個元素 append 進 results。

#### 空間複雜度:
不算 results 的話 $\mathcal{O}(k)$，因為 curr 要存 k 個元素。算 results 的話 $\mathcal{O}(k \binom{n}{k})$。

#### reference:
https://youtu.be/q0s6m7AiM7o?t=288
    