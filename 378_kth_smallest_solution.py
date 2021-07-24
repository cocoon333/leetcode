# this solution is incorrect

"""
Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.
"""

import bisect
class Solution:
    def kthSmallest(self, matrix, k):
        lo, hi = matrix[0][0], matrix[len(matrix)-1][len(matrix[0])-1]
        while lo < hi:
            count = 0
            mid = lo + (hi - lo) // 2
            for i in range(len(matrix)):
                count += matrix[i].bisect(matrix[i], mid)
            if count < k:
                low = mid + 1
            else:
                hi = mid
        return lo
