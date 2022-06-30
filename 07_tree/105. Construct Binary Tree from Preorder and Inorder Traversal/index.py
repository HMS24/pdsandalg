"""https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""

class Solution_1:
    def buildTree(self, preorder, inorder):
        if not preorder:
            return
        val = preorder[0]
        root = TreeNode(val)
        pos = self.__get_position(nums=inorder, target=val)
        root.left = self.buildTree(preorder[1:pos+1], inorder[0:pos])
        root.right = self.buildTree(preorder[pos+1:], inorder[pos+1:])
        return root

    def __get_position(self, nums, target):
        for i, num in enumerate(nums):
            if num == target:
                return i

        # 題目的 binary tree nums 是 tree node 的編號，非 val
        # 因此 inorder nums 並非代表實際的 val 順序。
        # start, end = 0, len(nums)-1

        # while start <= end:
        #     mid = (start + end) // 2
        #     if nums[mid] == target:
        #         return mid
            
        #     if nums[mid] > target:
        #         end = mid - 1
        #     else:
        #         start = mid + 1
