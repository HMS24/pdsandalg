"""https://leetcode.com/problems/decode-ways/submissions/
"""


class Solution1:
    def decodeWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        cache = [-1] * n

        def num_decodings(pointer):
            if pointer >= n:
                return 1
            if cache[pointer] > -1:
                return cache[pointer]

            total_decompositions = 0
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
