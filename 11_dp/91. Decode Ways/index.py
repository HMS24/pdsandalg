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
