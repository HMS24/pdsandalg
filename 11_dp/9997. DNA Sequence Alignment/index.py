"""
DNA Sequence Alignment


https://www.youtube.com/watch?v=SYBmn3Q_S6s
"""

# recursion
class Solution1:
    """
    e.g.
    GACGTTA
    i
    GAACGCTA
    j

    steps (i, j)
    1. match (i+1, j+1) cost 0
    2. match (i+1, j+1) cost 0
    3. C, A
        - s1 GAP (i, j+1) cost 1            @use
        - s2 GAP (i+1, j) cost 1 
        - mismatch (i+1, j+1) cost x
    4. match (i+1, j+1) cost 0
    5. match (i+1, j+1) cost 0
    6. T, C
        - s1 GAP (i, j+1)  cost 1             @use
        - s2 GAP (i+1, j). cost 1   
        - mismatch (i+1, j+1) cost x
    7. match (i+1, j+1) cost 0
    8. T, A
        - s1 GAP (i, j+1)  cost 1             @use
        - s2 GAP (i+1, j). cost 1   
        - mismatch (i+1, j+1) cost x
    9. T, ""
        - add s1 length gap on s2 cost 2

    cost = 1+1+1+2 = 5

    時間複雜度
        m = len(s1)
        n = len(s2)

        最糟情況序列均不同
        每對 pair 都要 call rec 3 次
        直到 base case 一方為 empty string
        高度有 n 階 因此為 O(3^n)
    空間複雜度
        單純 function call 的 stack 深度 O(n)
        每個 node 僅為 O(1) 的 work
    """
    GAP_COST = 1
    alignment_costs = {}

    def __init__(self):
        self.initialize_alignment_costs()

    def min_cost_alignment(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        def rec(i, j):
            # "", abc => 3
            if i == len(s1):
                return len(s2) - j
            if j == len(s2):
                return len(s1) - i
            if s1[i] == s2[j]:
                return rec(i+1, j+1)

            # 3 種方法 s1 加 gap, s2 加 gap or just mismatch each other
            gap_s1 = self.GAP_COST + rec(i, j+1)
            gap_s2 = self.GAP_COST + rec(i+1, j)
            
            mismatch_pair = s1[i]+s2[j]
            mismatch = self.alignment_costs[mismatch_pair] + rec(i+1, j+1)

            return min(gap_s1, gap_s2, mismatch)
        return rec(0, 0)

    def initialize_alignment_costs(self):
        self.alignment_costs["AA"] = 0
        self.alignment_costs["CC"] = 0
        self.alignment_costs["GG"] = 0
        self.alignment_costs["TT"] = 0

        self.alignment_costs["AC"] = 1
        self.alignment_costs["CA"] = 1

        self.alignment_costs["AG"] = 2
        self.alignment_costs["GA"] = 2

        self.alignment_costs["AT"] = 4
        self.alignment_costs["TA"] = 4

        self.alignment_costs["CG"] = 3
        self.alignment_costs["GC"] = 3

        self.alignment_costs["CT"] = 5
        self.alignment_costs["TC"] = 5

        self.alignment_costs["GT"] = 1
        self.alignment_costs["TG"] = 1

if __name__ == "__main__":
    assert 3 == Solution1().min_cost_alignment("GACGTTA", "GAACGCTA")