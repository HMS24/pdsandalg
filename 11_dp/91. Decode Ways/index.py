"""https://leetcode.com/problems/decode-ways/submissions/
"""


class Solution1:
    def decodeWays(self, s):
        """
            223
            可以 decompose 

            - level 1
                1 character
                    2 23
                2 character
                    22 3

            level 2
                1 character
                    2 2 3 
                    pointer at 3
                2 character
                    2 23
                    pointer at empty string 超過 str 的 len so return 1

            level 3
                1 character
                    2 2 3
                    pointer at empty string return 1

            time complexity: 
                如果沒有 memorized 每次 pointer 都會拆成 2 半
                `O(2^n)`
                不過因為加了 cache ，把子問題解決了等於 cut off tree 的一半，pointer 就跟 iteration 一樣
                through all indices
                `O(n)`

            space complexity:
                maintain 一個 list 及 n 個 O(1) work 的 function call stack
                O(n)
        """
        n = len(s)
        cache = [-1] * n

        def num_decodings(pointer):
            # base case 超過 str len
            if pointer >= n:
                return 1
            if cache[pointer] > -1:
                return cache[pointer]

            total_decompositions = 0
            # 可以 decompose 1 or 2 characters
            for i in range(1, 2+1):
                if pointer + i > n:
                    break

                snippet = s[pointer:pointer+i]
                if is_valid(snippet):
                    total_decompositions += num_decodings(pointer+i)

            cache[pointer] = total_decompositions

            return total_decompositions

        def is_valid(snippet):
            if not snippet or snippet == "0" or snippet[0] == "0":
                return False
            return int(snippet) in range(1, 26+1)

        num_decodings(0)
        return cache[0]
