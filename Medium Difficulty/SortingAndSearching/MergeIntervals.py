class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        size = len(intervals)
        if size == 1:
            return intervals

        self.mergeSortIntervals(intervals)

        res = [intervals[0]]

        for i in range(1,size):

            if res[-1][1] >= intervals[i][0]:
                res[-1] = [min(res[-1][0],intervals[i][0]),intervals[i][1]]

            else:
                res.append(intervals[i])
            res = self.checkBackRes(res)

        return res

    def checkBackRes(self,res):
        new_res = [res[-1]]

        modified = False
        size = len(res)

        current = -2

        while current >= -size:

            if res[current][1] >= new_res[0][0]:
                modified = True
                new_res[0] = [min(res[current][0],new_res[0][0]),new_res[0][1]]
                current -= 1
            else:
                if modified:
                    new_res = res[:current+1] + new_res
                    return new_res
                return res

        return new_res
    def mergeSortIntervals(self,array):
        helper = [[0,0] for i in range(len(array))]
        self.mergeSort(array,helper,0,len(array)-1)

    def mergeSort(self,array,helper,low,high):
        if low < high:
            middle = (low + high)//2
            self.mergeSort(array,helper,low,middle)
            self.mergeSort(array,helper,middle+1,high)
            self.mergeS(array,helper,low,middle,high)

    def mergeS(self,array,helper,low,middle,high):
        for i in range(low,high+1):
            helper[i] = array[i]

        current_left = low
        current_right = middle + 1
        current = low
        while (current_left <= middle and current_right <= high ):
            if helper[current_left][1] <= helper[current_right][1]:
                array[current] = helper[current_left]
                current_left += 1
            else:
                array[current] = helper[current_right]
                current_right += 1
            current += 1

        while current_left <= middle:
                array[current] = helper[current_left]
                current += 1
                current_left += 1


sol = Solution()

print(sol.merge([[2,3],[4,5],[6,7],[8,9],[1,10],[0,12]]))