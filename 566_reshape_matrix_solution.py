"""
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the row number and column number of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
"""

class Solution:
    def matrixReshape(self, mat, r, c):
        if (len(mat) * len(mat[0]) != r * c):
            return mat

        res = []
        mat_i = 0
        mat_j = 0
        for i in range(r):
            res.append([])
            for j in range(c):
                if mat_j >= len(mat[0]):
                    mat_i += 1
                    mat_j = 0

                res[-1].append(mat[mat_i][mat_j])
                mat_j += 1

        return res

if (__name__ == "__main__"):
    S = Solution()
    print(S.matrixReshape([[1, 2], [3, 4]], 1, 4))
    print(S.matrixReshape([[1, 2], [3, 4]], 2, 4))
