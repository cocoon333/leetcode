"""
Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
"""

class Solution:
    def triangleNumber(self, nums):
        if len(nums) < 2:
            return 0

        nums.sort()
        res = 0
        for i in range(2, len(nums)):
            hi = i-1
            lo = 0
            while hi > lo:
                if nums[lo] + nums[hi] > nums[i]:
                    res += hi - lo
                    hi -= 1
                else:
                    lo += 1
        return res

if (__name__ == "__main__"):
    S = Solution()
    assert(S.triangleNumber([4, 2, 3, 4]) == 4)
    assert(S.triangleNumber([2, 2, 3, 4]) == 3)
    assert(S.triangleNumber([3, 4]) == 0)
