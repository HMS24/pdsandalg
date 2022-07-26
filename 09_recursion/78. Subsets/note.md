## Approach 1

Cascading

對每個元素套用有無的概念

e.g. 
nums = [1, 2, 3]
- ${2}^{0}$: `[]`
- ${2}^{1}$: `[], [1]`
- ${2}^{2}$: `[], [1], [2], [1, 2]`
- ${2}^{3}$: `[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]`

```python
class Solution1:
    def subsets(self, nums):
        results  = [[]]
        for num in nums:
            results += [item+[num] for item in results]
        return results
```

#### 時間複雜度:
執行 n 回合，每一回合都加入新的 num，為 2 的指數增加。因此需耗費 $\mathcal{O}(n*{2}^{n})$。

#### 空間複雜度:
3 個數字會有 ${2}^{n}$ 個 subsets，而每個回合也都要新增 list 來 extend 這些 subsets。$\mathcal{O}(n*{2}^{n})$。


## Approach 2

Backtracking

首先每次進入 function 就將 curr append into results，
接下來慢慢加入 num 帶入下一個 function call 
離開時在 pop 掉

```python
class Solution2:
    def subsets(self, nums):
        results = []

        def backtrack(start, curr):
            results.append(curr[:])

            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtrack(i+1, curr)
                curr.pop()

        backtrack(0, [])
        return results
```

#### 時間複雜度:
會產生 ${2}^{n}$ 個 subsets，又每次產生的 subset 需 copy 進 results，因此需耗費 $\mathcal{O}(n*{2}^{n})$。

#### 空間複雜度:
只需要維護 curr 的 list 空間，為 $\mathcal{O}(n)$