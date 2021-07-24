"""
Shortest Unsorted Continuous Subarray

Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.
"""
class Solution:
    def findUnsortedSubarray_failed(self, nums):
        i = 0
        j = len(nums) - 1
        old_i = -1
        old_j = -1
        while i < j:
            if nums[i] <= nums[i+1]:
                if nums[i] == nums[i+1] and old_i < 0:
                    old_i = i
                elif not(nums[i] == nums[i+1]):
                    old_i = -1
                i += 1
            elif nums[j] >= nums[j-1]:
                if nums[j] == nums[j-1] and old_j < 0:
                    old_j = j
                elif not(nums[j] == nums[j-1]):
                    old_j = -1
                j -= 1
            else:
                break


        if not(j == i):
            if old_i > 0: i = old_i
            if old_j > 0: j = old_j
            j += 1
        return j - i
    
    def findUnsortedSubarray(self, nums):
        s_nums = sorted(nums)
        start = -1
        end = len(nums) - 1
        for i in range(len(nums)):
            if not(nums[i] == s_nums[i]):
                if start < 0:
                    start = i
                end = i

        if start < 0: return 0
        return end - start + 1

if __name__ == "__main__":
    S = Solution()
    l1 = [2, 6, 4, 8, 10, 9, 15]
    l2 = [2]
    l3 = [1, 2, 3]
    l4 = [3, 2, 1]
    l5 = [1, 3, 5, 4]
    l6 = [1, 3, 2, 2, 2]
    l7 = [1, 2, 3, 3, 3]

    print(S.findUnsortedSubarray(l1))
    print(S.findUnsortedSubarray(l2))
    print(S.findUnsortedSubarray(l3))
    print(S.findUnsortedSubarray(l4))
    print(S.findUnsortedSubarray(l5))
    print(S.findUnsortedSubarray(l6))
    print(S.findUnsortedSubarray(l7))
