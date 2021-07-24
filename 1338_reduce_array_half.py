"""
Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.
"""

from collections import Counter
class Solution:
    def minSetSize(self, arr):
        c = Counter(arr)
        target = len(arr) // 2
        count = 0
        for i in sorted(c.values(), reverse=True):
            if target > 0:
                target -= i
                count += 1
            else:
                    break
        return count

if (__name__ == "__main__"):
    S = Solution()
    assert(S.minSetSize([3,3,3,3,5,5,5,2,2,7]) == 2)
    assert(S.minSetSize([7, 7, 7, 7, 7, 7]) == 1)
    assert(S.minSetSize([1, 9]) == 1)
    assert(S.minSetSize([1000, 1000, 3, 7]) == 1)
    assert(S.minSetSize([1,2,3,4,5,6,7,8,9,10]) == 5)
