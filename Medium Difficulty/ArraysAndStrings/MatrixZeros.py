class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        rows_size = len(matrix)
        cols_size = len(matrix[0])
        zero_cols = set()

        i = 0
        while (i < rows_size):

            # go through row
            j = 0
            empty_row = False
            while (j < cols_size):
                if matrix[i][j] == 0:
                    zero_cols.add(j)
                    empty_row = True
                j += 1
            if empty_row:
                matrix[i] = [ 0 ]*len(matrix[i])
            i += 1

        for j in zero_cols:
            for i in range(rows_size):
                matrix[i][j] = 0





sol = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
sol.setZeroes([[1,1,1],[1,0,1],[1,1,1]])
print(matrix)