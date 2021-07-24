"""
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.

"""
class Solution:

    def findPeakElement(self, nums):
        return self.recursive_find(nums, 0, len(nums)-1)

   

    def recursive_find(self, nums, lo, hi):
        if lo == hi:
            return lo
        if hi - lo == 1:
            if nums[hi] > nums[lo]:
                return hi
            return lo

        mid = lo + (hi - lo) // 2

        if nums[mid-1] > nums[mid]:
            res = self.recursive_find(nums, lo, mid-1)
            if res >= 0:
                return res

        if nums[mid+1] > nums[mid]:
            res = self.recursive_find(nums, mid+1, hi)
            return res

        return mid

if (__name__ == "__main__"):
    S = Solution()
    assert(S.findPeakElement([1, 2, 3, 1]) == 2)
    assert(S.findPeakElement([1, 2]) == 1)
    assert(S.findPeakElement([1]) == 0)
    assert(S.findPeakElement([1, 2, 1, 3, 5, 6, 4]) == 5)
