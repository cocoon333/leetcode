"""
Given an array nums, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.

"""

class Solution:
    def partitionDisjoint(self, nums):
        if not len(nums):
            return 0

        i = 0
        j = len(nums)-1
        max_left = nums[i]
        min_right = nums[j]
        min_index = j
        while i < j:
            print(i, j)
            if nums[j] >= nums[i]:
                if nums[j] < min_right:
                    min_right = nums[j]
                    min_index = j
                j -= 1
            else:
                i += 1
                if nums[i] > min_right:
                    max_left = nums[i]
                    min_right = len(nums) - 1
                    j = len(nums) - 1


        return j + 1


if __name__ == "__main__":
    S = Solution()
    print(S.partitionDisjoint([1, 1, 1, 0, 6, 12]))
    assert(S.partitionDisjoint([1, 1, 1, 0, 6, 12]) == 4)
    assert(S.partitionDisjoint([5, 0, 3, 8, 6]) == 3)
    assert(S.partitionDisjoint([5, 7, 6, 5]) == 1)
    assert(S.partitionDisjoint([]) == 0)
    assert(S.partitionDisjoint([9, 3, 4, 7, 8]) == 5)
    assert(S.partitionDisjoint([4, 7, 6, 6, 6]) == 1)
    assert(S.partitionDisjoint([4, 7, 0, 6, 6]) == 5)
