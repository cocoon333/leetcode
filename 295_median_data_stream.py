"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
"""

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []


    def addNum(self, num):
        self.l.insert(bisect_left(self.l, num), num)


    def findMedian(self):
        if (len(self.l) % 2):
            return self.l[len(self.l) // 2]
        else:
            return (self.l[len(self.l) // 2] + self.l[len(self.l) // 2 - 1]) / 2


class MedianFinderOptimized:
    #incorrect

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = [0] * 103


    def addNum(self, num):
        if (0 <= num <= 100):
            self.l[num+1] += 1
        elif (num < 0):
            self.l[0] += 1
        else:
            self.l[-1] += 1


    def findMedian(self):
        i = 0
        i_non_zero = 0
        j = len(self.l) - 1
        j_non_zero = 0
        count = 0
        while (i < j):
            while (count <= 0 and i < j):
                count += self.l[i]
                i += 1
                if self.l[i] > 0:
                    i_non_zero += 1
            while (count >= 0 and i < j):
                count -= self.l[j]
                j -= 1
                if self.l[j] > 0:
                    j_non_zero -= 1
        if count:
            return i_non_zero
        return (i_non_zero + j_non_zero) / 2
