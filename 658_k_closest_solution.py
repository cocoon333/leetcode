"""
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
"""
class Solution:

    def findClosestElements(self, arr, k, x):

        lo = self.binarySearch(arr, x, 0, len(arr)-1)

        hi = lo + 1
        loChangedLast = False

        for i in range(k):
            if (lo < 0):
                loChangedLast = False
                hi += 1

            elif (hi >= len(arr)):
                loChangedLast = True
                lo -= 1

            elif (abs(x - arr[lo]) <= abs(x - arr[hi])):
                loChangedLast = True
                lo -= 1

            else:
                loChangedLast = False
                hi += 1

        return arr[lo+1:hi]

       

    def binarySearch(self, arr, x, lo, hi):
        if (hi - lo <= 1):
            return lo

        mid = (lo + hi) // 2

        if (x > arr[mid]):
            lo = mid
        else:
            hi = mid

        return self.binarySearch(arr, x, lo, hi)
