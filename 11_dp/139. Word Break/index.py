"""https://leetcode.com/problems/word-break/
"""


class Solution1:
    """
        hello
        [h, e, llo]

        index 把每個 char 當作最後一個 char
        再依序拆成 prefix and suffix 看有無在裡面
        並且 cache prefix 可不可以 decompose

        i = 1
            j = 0
                prefix = can decompose "" ? T
                suffix = "h" in dictionary ? T
                cache[1] = T

        i = 2
            j = 0
                prefix = can decompose "" ? T
                suffix = "he" in dictionary ? F
            j = 1
                prefix = can decompose "h" ? T
                suffix = "e" in dictionary ? T
                cache[1] = T

        i = 3
            j = 0
                prefix = can decompose "" ? T
                suffix = "hel" in dictionary ? F
            j = 1
                prefix = can decompose "h" ? T
                suffix = "el" in dictionary ? F
            j = 2
                prefix = can decompose "he" ? T
                suffix = "l" in dictionary ? F
        ...
        ...
    """
    def wordBreak(self, s, wordDict):
        can_decompose = [False] * (len(s)+1)
        
        # 可以 decompose empty string "" by using no words in deictionary.
        can_decompose[0] = True

        for i in range(1, len(s)+1):
            for j in range(0, i):
                prefix_in_dict = can_decompose[j]
                suffix_in_dict = s[j:i] in wordDict

                if prefix_in_dict and suffix_in_dict:
                    can_decompose[i] = True

                    break
        return can_decompose[-1]
