## 01 Preview
* [[66. Plus One]](./01_preview/66.%20Plus%20One/index.py)  [[Note]]()

## 02 Search
* [[35. Search Insert Position]](./02_search/35.%20Search%20Insert%20Position/index.py)  [[Note]]()
* [[278. First Bad Version]](./02_search/278.%20First%20Bad%20Version/index.py)  [[Note]]()
* [[561. Array Partition I]](./02_search/561.%20Array%20Partition%20I/index.py)  [[Note]]()
* [[704. Binary Search]](./02_search/704.%20Binary%20Search/index.py)  [[Note]]()
* [[852. Peak Index in a Mountain Array]](./02_search/852.%20Peak%20Index%20in%20a%20Mountain%20Array/index.py)  [[Note]]()

## 03 String
* [[344. Reverse String]](./03_string/344.%20Reverse%20String/index.py)  [[Note]]()
* [[1160. Find Words That Can Be Formed by Characters]](./03_string/1160.%20Find%20Words%20That%20Can%20Be%20Formed%20by%20Characters/index.py) [[Note]]()

## 04 Array
* [[26. Remove Duplicates from Sorted Array]](./04_array/26.%20Remove%20Duplicates%20from%20Sorted%20Array/index.py)  [[Note]]()
* [[287. Find the Duplicate Number]](./04_array/287.%20Find%20the%20Duplicate%20Number/index.py)  [[Note]]()
* [[442. Find All Duplicates in an Array]](./04_array/442.%20Find%20All%20Duplicates%20in%20an%20Array/index.py)  [[Note]]()

## 05 Map and Set
* [[15. 3Sum]](./05_map_and_set/15.%203Sum/index.py)  [[Note]]()
* [[49. Group Anagrams]](./05_map_and_set/49.%20Group%20Anagrams/index.py)  [[Note]]()
* [[80. Remove Duplicates from Sorted Array II]](./05_map_and_set/80.%20Remove%20Duplicates%20from%20Sorted%20Array%20II/index.py)  [[Note]]()
* [[136. Single Number]](./05_map_and_set/136.%20Single%20Number/index.py)  [[Note]]()
* [[167. Two Sum II - Input array is sorted]](./05_map_and_set/167.%20Two%20Sum%20II%20-%20Input%20array%20is%20sorted/index.py)  [[Note]]()
* [[242. Valid Anagram]](./05_map_and_set/242.%20Valid%20Anagram/index.py)  [[Note]]()
* [[260. Single Number III]](./05_map_and_set/260.%20Single%20Number%20III/index.py)  [[Note]]()
* [[961. N-Repeated Element in Size 2N Array]](./05_map_and_set/961.%20N-Repeated%20Element%20in%20Size%202N%20Array/index.py)  [[Note]]()

## 06 Linked List
* [[2. Add Two Numbers]](./06_linked_list/2.%20Add%20Two%20Numbers/index.py)  [[Note]]()
* [[21. Merge Two Sorted Lists]](./06_linked_list/21.%20Merge%20Two%20Sorted%20Lists/index.py)  [[Note]](https://hackmd.io/KzJHYRmRTdyfZA2xRfNMSw)
* [[83. Remove Duplicates from Sorted List]](./06_linked_list/83.%20Remove%20Duplicates%20from%20Sorted%20List/index.py)  [[Note]]()
* [[142. Linked List Cycle II]](./06_linked_list/142.%20Linked%20List%20Cycle%20II/index.py)  [[Note]]()
* [[148. Sort List]](./06_linked_list/148.%20Sort%20List/index.py)  [[Note]](https://hackmd.io/xie4spD_T_KfNJhq18KpKQ)
* [[206. Reverse Linked List]](./06_linked_list/206.%20Reverse%20Linked%20List/index.py)  [[Note]]()
* [[725. Split Linked List in Parts]](./06_linked_list/725.%20Split%20Linked%20List%20in%20Parts/index.py)  [[Note]]()

## 07 Tree
* [[94 Binary Tree Inorder Traversal]](./07_tree//94.%20Binary%20Tree%20Inorder%20Traversal/index.py)  [[Note]]()
    inorder traversal 使用 iterative ! 有點難想
    ref: Approach2 Iterate
* [[100 Same Tree]](./07_tree//100.%20Same%20Tree/index.py)  [[Note]]()
    * 回傳物件要一致
        在 depth == 0 時，不能只有 return  [[Note]]()
        否則當 tree 只有 root １節點時會 runtime error
    * 更好的方法：遞迴每個節點就好！！看 solution 才知道...  [[Note]]()
* [[102. Binary Tree Level Order Traversal]](./07_tree//102.%20Binary%20Tree%20Level%20Order%20Traversal/index.py)  [[Note 未完]](https://hackmd.io/ccXwdNbHSx6s1s3LMj2NlQ)
* [[104. Maximum Depth of Binary Tree]](./07_tree/104.%20Maximum%20Depth%20of%20Binary%20Tree/index.py)  [[Note]]()
* [[111. Minimum Depth of Binary Tree]](./07_tree//111.%20Minimum%20Depth%20of%20Binary%20Tree/index.py)  [[Note]]()
    1. Approach 2 Recursion 深度優先 優化！
* [[124. Binary Tree Maximum Path Sum]](./09_recursion//124.%20Binary%20Tree%20Maximum%20Path%20Sum/index.py)  [[Note]]()
    * Approach 1 recursion
        模式很難辨識...  [[Note]]()
        要從最少3個節點開始想
        遞迴到最底層回傳 path
        紀錄可能單邊出現的最大值
* [[144. Binary Tree Preorder Traversal]](./07_tree//144.%20Binary%20Tree%20Preorder%20Traversal/index.py)  [[Note 未完]](https://hackmd.io/1b3OJV4cRCWS_j_kkIMBzQ)
* [[236. Lowest Common Ancestor of a Binary Tree]](./09_recursion//236.%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree/index.py)  [[Note]]()
    * Approach 1 recursion
        dfs 想很久...  [[Note]]()
        要傳進一個 res 當作找到路徑的結果
        這樣判斷才不會找到又繼續跑
* [[1382 Balance a Binary Search Tree]](./07_tree//1382.%20Balance%20a%20Binary%20Search%20Tree/index.py)  [[Note]]()
    * 一開始的方式不穩定，是錯誤的
      對每個節點算出左右子樹高度差，
      然後辨別型態，再 rotate，  [[Note]]()
      結果發現 root 不平衡。
    * 重新排序中序遍歷，再新增 balance tree!  [[Note]]()

## 08 Stack and Queue
* [[0. queue_using_list]](./08_stack_and_queue/0.%20queue_using_list/index.py)  [[Note]]()
* [[0. stack_using_list]](./08_stack_and_queue/0.%20stack_using_list/index.py)  [[Note]]()
* [[225. Implement Stack using Queues]](./08_stack_and_queue/225.%20Implement%20Stack%20using%20Queues/index.py)  [[Note]]()

## 09 Recursion
* [[24. Swap Nodes in Pairs]](./09_recursion/24.%20Swap%20Nodes%20in%20Pairs/index.py)  [[Note]]()
* [[40. Combination Sum II]](./09_recursion//40.%20Combination%20Sum%20II/index.py)  [[Note]](https://hackmd.io/ZcK7IEXSTiiGGUUN7YXIsw)
* [[54. Spiral Matrix]](./09_recursion//54.%20Spiral%20Matrix/index.py)  [[Note]](https://hackmd.io/3em6KeTGTS2XTmhh5u3lmg)
* [[77. Combinations]](./09_recursion//77.%20Combinations/index.py)  [[Note]](https://hackmd.io/0RYLEAdvSt-U1prTlR-74A)
* [[78. Subsets]](./09_recursion//78.%20Subsets/index.py)  [[Note]]()
    * Approach 1 iteration  [[Note]]()
        * 構造 power set 有一套固定的思維, 從空集合開始, 選擇包含某個元素或者不包含, 每次選擇會增加 2 種可能, 因此會讓set 的數目不斷乘2 
    * Approach 2 recursion  [[Note]]()
        * dfs 記錄走過的路徑
    * Approach 3 backtracking  [[Note]]()
        * 球池不斷丟球 > 判斷符合數量 > 取球  [[Note]]()
        * 時間複雜度:
            不好估算，可以取大概即可    [[Note]]()
            <img src="https://i.imgur.com/wLEFtDI.jpg" alt="_" width="480" height="200"/>
* [[113. Path Sum II]](./09_recursion//113.%20Path%20Sum%20II/index.py)  [[Note]](https://hackmd.io/XgQPsr40TO-y65ObjHhKpA)
* [[698. Partition to K Equal Sum Subsets]](./09_recursion//698.%20Partition%20to%20K%20Equal%20Sum%20Subsets/index.py) [[Note 未完]](https://hackmd.io/wyFlT5PASsmaG-uMP2bEyQ)

## 10 Graph
* [[133. Clone Graph]](./08_graph//133.%20Clone%20Graph/index.py)  [[Note 未完]](https://hackmd.io/czrnXN2tSzmku8il2GMvhQ)
* [[207. Course Schedule]](./08_graph/207.%20Course%20Schedule/index.py)  [[Note 未完]](https://hackmd.io/_HDprlaHTRyXI_h7Sc-DLA?both)
* [[1091. Shortest Path in Binary Matrix]](./08_graph//1091.%20Shortest%20Path%20in%20Binary%20Matrix/index.py)  [[[Note 未完]](https://hackmd.io/UQHaj4bgQw2LBWfZwz0gFA)