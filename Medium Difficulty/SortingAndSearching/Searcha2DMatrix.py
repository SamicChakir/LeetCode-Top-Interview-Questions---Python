
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        size_lig = len(matrix)
        size_col = len(matrix[0])
        return self.search_rec_Matrix(0,size_lig-1,0,size_col-1,matrix,target)

    def search_rec_Matrix(self,low_i,high_i,low_j,high_j,matrix,target):

        if low_i <= high_i and low_j <= high_j:
            middle_i = (low_i + high_i) // 2
            middle_j = (low_j + high_j)//2
            middle_val = matrix[middle_i][middle_j]
            if middle_val < target:
                #we are very sure target wont bet ween low_i and middle_i and low_j and middle_j because all of this elements are smaller then middle val
                # we are left with low_i middle_i and middle_j+1 high_j
                # and middle_i+1 high_i and low_j high_j
                return self.search_rec_Matrix(low_i,middle_i,middle_j+1,high_j,matrix,target) \
                       or self.search_rec_Matrix(middle_i+1,high_i,low_j,high_j,matrix,target)
            elif middle_val > target:
                # we are very sure target wont be between middle_i and high_i and middle_j and high_j be cause all value in this range ar bigger then middle val
                # we are left with middle_i to high_i and low_j to middle_j-1
                # and low_i to middle_i - 1 and low_j to high_j
                return self.search_rec_Matrix(middle_i,high_i,low_j,middle_j-1,matrix,target) \
                       or self.search_rec_Matrix(low_i,middle_i-1,low_j,high_j,matrix,target)
            else:
                return True


        return False

sol = Solution()
print(sol.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))
# while low_i <= high_i: # search in One line
#     middle = (low_i + high_i) // 2
#
#     middle_val = matrix[middle][low_j]
#     if middle_val == target:
#         return True
#     elif middle_val > target:
#         high_i = middle - 1
#     else:
#         low_i = middle + 1
#
# while low_j <= high_j:#search in One Column
#     middle = (low_j + high_j)//2
#     middle_val = matrix[low_i][middle]
#     if middle_val == target:
#             return True
#     elif middle_val > target:
#             high_j = middle - 1
#     else:
#             low_j = middle + 1