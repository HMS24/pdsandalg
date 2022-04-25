* 6 tree
    * [94 Binary Tree Inorder Traversal](./6_stack-queue-tree/94.%20Binary%20Tree%20Inorder%20Traversal/index.py)
        inorder traversal 使用 iterative ! 有點難想
        ref: Approach2 Iterate
    * [100 Same Tree](./6_stack-queue-tree/100.%20Same%20Tree/index.py)
        1. 回傳物件要一致
            在 depth == 0 時，不能只有 return
            否則當 tree 只有 root １節點時會 runtime error
        2. 更好的方法：遞迴每個節點就好！！看 solution 才知道...
    * [1382 Balance a Binary Search Tree](./6_stack-queue-tree/1382.%20Balance%20a%20Binary%20Search%20Tree/index.py)
        1. 一開始的方式不穩定，是錯誤的
            對每個節點算出左右子樹高度差，
            然後辨別型態，再 rotate，
            結果發現 root 不平衡。
        2. 重新排序中序遍歷，再新增 balance tree!