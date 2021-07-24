"""
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.
"""

class Solution:
    def findLength(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        dp = [[0] * len2 for i in range(len1)]
        res = 0
        for i in range(len1):
            for j in range(len2):
                if (nums1[i] == nums2[j]):
                    if (i == 0 or j == 0):
                        dp[i][j] = 1
                        res = max(res, dp[i][j])
                    else:
                        dp[i][j] = dp[i-1][j-1] + 1
                        res = max(res, dp[i][j])
        return res

if (__name__ == "__main__"):
    S = Solution()
    assert(S.findLength([1,2,3,2,1], [3,2,1,4,7]) == 3)
    assert(S.findLength([0,0,0,0,0], [0,0,0,0,0]) == 5)
    assert(S.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4]) == 3)
