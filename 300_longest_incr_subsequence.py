#incorrect
"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
"""

class Solution:
    def lengthOfLIS(self, nums):
        sub=[]
        for num in nums:
            i = bisect_left(sub, num)
            if i == len(sub):
                sub.append(num)
            else:
                sub[i] = num
        return len(sub)

if (__name__ == "__main__"):
    S = Solution()
#    assert(S.lengthOfLIS([10, 9, 2, 5, 3, 4]) == 3)
#    assert(S.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4)
    assert(S.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4)
    assert(S.lengthOfLIS([7, 7, 7]) == 1)
