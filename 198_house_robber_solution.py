"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""

class Solution:
    def rob(self, nums):
        max_with_recent = 0
        max_without_recent = 0
        for i in range(len(nums)):
            if max_without_recent + nums[i] > max_with_recent:
                temp = max_without_recent
                max_without_recent = max_with_recent
                max_with_recent = temp + nums[i]
            else:
                max_without_recent = max_without_recent
                max_with_recent = max_with_recent - nums[i-1] + nums[i]
        return max(max_with_recent, max_with_recent)

if __name__ == "__main__":
    S = Solution()
    print(S.rob([1, 2, 3, 1]))
    assert(S.rob([2, 7, 9, 3, 1]) == 12)
