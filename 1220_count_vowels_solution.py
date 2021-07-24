"""
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.
"""

class Solution:
    def countVowelPermutation(self, n):
        res = [1] * 5
        for i in range(n-1):
            a, e, i, o, u = res
            res[0] = e + i + u
            res[1] = a + i
            res[2] = e + o
            res[3] = i
            res[4] = o + i
        return sum(res) % (10 ** 9 + 7)

if (__name__ == "__main__"):
    S = Solution()
    assert(S.countVowelPermutation(5) == 68)
    assert(S.countVowelPermutation(1) == 5)
    assert(S.countVowelPermutation(2) == 10)
