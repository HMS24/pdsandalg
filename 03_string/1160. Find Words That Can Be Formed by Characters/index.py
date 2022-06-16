"""https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
"""
from typing import List

# Approach 1
"""
1. 計算字元出現次數並存成 hash table
2. 對 list 中每個單字的字元，計算出現次數。
3. 該單字各字元出現次數與 hash table 次數比較，若大於則 break。
4. 該單字各字元均小於等於 hash table 次數則加總單字長度

def count(L, chars):
    sum = 0
    count_dict = {}
    for char in chars;
        count_dict[char] = chars.count(char)
    
    for word in L:
        for char in word:
            if word.count(char) > count_dict[char]:
                break
        else:
            sum += 1
    return sum
"""


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sum = 0
        chars_count = {}
        for char in chars:
            if char not in chars_count:
                chars_count[char] = 1
            else:
                chars_count[char] += 1

        for word in words:
            for char in word:
                count = chars_count.get(char, 0)
                if word.count(char) > count:
                    break
            else:
                sum += len(word)

        return sum
