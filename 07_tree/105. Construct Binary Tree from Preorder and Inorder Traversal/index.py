"""https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""

from helper import TreeNode


class Solution1:
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


class Solution2:
    """
    優化 Solution1

    * __get_position > hash map
    * slice list > pointer
    """

    def buildTree(self, preorder, inorder):
        index = 0
        index_cache = {val: i for i, val in enumerate(inorder)}

        def create_node(left, right):
            nonlocal index

            if left > right:
                return None

            val = preorder[index]
            index += 1

            root = TreeNode(val)
            pos = index_cache[val]
            root.left = create_node(left, pos-1)
            root.right = create_node(pos+1, right)
            return root

        return create_node(0, len(inorder)-1)
