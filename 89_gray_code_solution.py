"""
An n-bit gray code sequence is a sequence of 2n integers where:

Every integer is in the inclusive range [0, 2n - 1],
The first integer is 0,
An integer appears no more than once in the sequence,
The binary representation of every pair of adjacent integers differs by exactly one bit, and
The binary representation of the first and last integers differs by exactly one bit.
Given an integer n, return any valid n-bit gray code sequence.
"""

class Solution:
    def grayCodeSlow(self, n):
        flips = [0]
        for i in range(2, n+1):
            new_flips = []
            for j in flips:
                new_flips.append(i-1)
                new_flips.append(j)
            new_flips.append(i-1)
            flips = list(new_flips)

        res = ['0' * n] * (len(flips) + 1)
        for i in range(1, len(flips) + 1):
            prev = res[i-1]
            flip = flips[i-1]
            if (flip == n - 1):
                res[i] = prev[:-1] + str(int(not(int(prev[-1]))))
            else:
                res[i] = prev[:flips[i - 1]] + str(int(not(int(prev[flips[i - 1]])))) + prev[flips[i - 1] + 1:]
        
        for i in range(len(res)):
            res[i] = int(res[i], 2)

        return res

    def gayCode(self, n):
        res = [0]

        for i in range(1, n):
            mask

if (__name__ == "__main__"):
    S = Solution()
    print(S.grayCode(1))
    print(S.grayCode(2))
    print(S.grayCode(3))
    print(S.grayCode(4))
