"""https://leetcode.com/problems/binary-tree-maximum-path-sum/
"""


class Solution1:
    def maxPathSum(self, root):
        # negative infinity
        max_result = float('-inf')

        def get_max(root):
            nonlocal max_result

            if root is None:
                return 0

            # 負數不用考慮，因此與 0 做比較。
            left_max = max(0, get_max(root.left))
            right_max = max(0, get_max(root.right))

            # 與之前存的 max result 比較
            curr_max_path_sum = left_max + root.val + right_max
            max_result = max(max_result, curr_max_path_sum)

            # 構成 path 為左右子樹其一 node 與 root
            return root.val + max(left_max, right_max)

        get_max(root)

        return max_result
