"""
Verifying Character Ordering

Given a string s representing a new ordering of the lowercase English letters and an array A[] of strings, return true if and only if A[] is sorted in lexicographical order according to the ordering provided in s.


Input: s = "hlbcdefgijkmnopqrstuvwxzya", A[] = ["hello", "hey", "a"].
Output: true

Explanation:
Under the new ordering, the array A[] is sorted. Note that the letter 'h' comes before the letter 'a', and the letter 'l' comes before the letter 'y'. 

"""


class Solution:
    def verifyOrdering(self, A, ordering):
        """
        :type A: list of str
        :type ordering: str
        :rtype: bool
        """

        char_order_map = {char: index for index, char in enumerate(ordering)}

        def s1_less_than_s2(s1, s2):
            counter = 0

            while (counter < len(s1) and counter < len(s2)):
                if s1[counter] != s2[counter]:
                    return char_order_map[s1[counter]] < char_order_map[s2[counter]]

                counter += 1

            return len(s1) <= len(s2)

        for i in range(0, len(A)-1):
            s1, s2 = A[i], A[i+1]

            if not s1_less_than_s2(s1, s2):
                return False

        return True
