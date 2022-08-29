
"""
Heapsort
"""


class Solution:
    """
    - build heap
        - from middle calc left, right 
        - compare who wins root position
            - swap them
        - recursive subtree
    - placement
        - swap first and last
        - build again
    """

    def heapsort(self, arr):
        '''
        :type arr: list of int
        :rtype: list of int
        '''
        n = len(arr)
        # create max heap tree，從中間開始往 start move 即可 create 完 max heap tree
        for i in range(n//2, -1, -1):
            self.heapify(arr, i, n)

        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]

            # 最後一個不用排 已經 swap 最大，離開 heap
            self.heapify(arr, 0, i)

        return arr

    def heapify(self, arr, i, n):
        # map system
        root = i
        left = 2*i+1
        right = 2*i+2

        if left < n and arr[left] > arr[root]:
            root = left

        if right < n and arr[right] > arr[root]:
            root = right

        if root != i:
            arr[i], arr[root] = arr[root], arr[i]

            # re heapify subtree
            self.heapify(arr, root, n)
