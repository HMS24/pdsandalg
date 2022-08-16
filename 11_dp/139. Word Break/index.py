"""https://leetcode.com/problems/word-break/
"""


class Solution1:
    def wordBreak(self, s, wordDict):
        can_decompose = [False] * (len(s)+1)
        can_decompose[0] = True

        for i in range(1, len(s)+1):
            for j in range(0, i):
                prefix_in_dict = can_decompose[j]
                suffix_in_dict = s[j:i] in wordDict

                if prefix_in_dict and suffix_in_dict:
                    can_decompose[i] = True

                    break
        return can_decompose[-1]
