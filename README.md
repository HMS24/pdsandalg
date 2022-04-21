* 6 tree
    * 94. Binary Tree Inorder Traversal 
        inorder traversal 使用 iterative ! 有點難想
        ref: Approach2 Iterate
    * 100. Same Tree
        1. 回傳物件要一致
            在 depth == 0 時，不能只有 return
            否則當 tree 只有 root １節點時會 runtime error
        2. 更好的方法：遞迴每個節點就好！！看 solution 才知道...
         