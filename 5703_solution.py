"""
5703. Maximum Average Pass Ratio

There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes, where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.

You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.

The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.

Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted.
"""

class Solution:
    def maxAverageRatio(self, classes, extraStudents):
        ratios = {}
        for a_class in classes:
            ratios[a_class[0] / a_class[1]] = a_class

        for i in range(extraStudents):
            key = min(ratios)
            min_class = ratios[key]
            print(min_class)
            min_class[0] += 1
            min_class[1] += 1
            ratios.pop(key)
            ratios[min_class[0]/min_class[1]] = min_class
            print(ratios)

        return sum(ratios.keys()) / len(ratios)

if __name__ == "__main__":
    s = Solution()

    print(s.maxAverageRatio([[1,2],[3,5],[2,2]], 2))
    #print(s.maxAverageRatio([[2,4],[3,9],[4,5],[2,10]], 3))
