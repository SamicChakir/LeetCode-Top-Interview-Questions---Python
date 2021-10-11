import sys

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        """
        if ( len(nums) < 3):
            return False
        i = 0
        size = len(nums)
        start,second,end = -sys.maxsize, -sys.maxsize, -sys.maxsize
        start_found = False
        second_found = False
        temp_start,temp_second,temp_third = -sys.maxsize, -sys.maxsize, -sys.maxsize
        while i < size:
            if not start_found: # looking for start
                start = nums[i]
                start_found = True
            else:
                if second_found:
                    current = nums [i]
                    if current > start:
                        if current < second:
                            second = current
                        elif current > second:
                            return True # found triplets
                    elif current < start:  # this is the tricky part
                        if i == size - 1:
                            return False
                        next = nums[i+1]
                        if next < current:

                            while i < size and next <= current:
                                i += 1
                                if i == size - 1:
                                    return False
                                current = next
                                next = nums[i + 1]

                        if next > second: #triplets found
                            return True
                        else:
                            start,second = current,next


                else: #second not already found
                    if nums[i] > start:
                        second_found = True
                        second = nums[i]
                    else:
                        start = nums[i]
            i += 1
        return False


    def threeSum1(self,nums):
        if len(nums) < 3:
            return False

        min = nums[0]
        max = sys.maxsize
        size = len(nums)

        for i in range(1,size):
            cur = nums[i]

            if cur <= min:
                min = cur
            elif cur <= max:
                max = cur
            else:
                return True
        return False




sol = Solution()

#
# print(sol.threeSum1([3,2,6,1,5]))#False
# print(sol.threeSum1([3,2,6,15,5,-10,-9,-8]))#True
# print(sol.threeSum1([3,2,6,1,2,3]))#True
print(sol.threeSum1([3,2,6,0,5,1,5]))#True
# print(sol.threeSum1([1,2,3,4,5]))#True
# print(sol.threeSum1([5,4,3,2,1]))#False
# print(sol.threeSum1([2,1,5,0,4,6]))#True
# print(sol.threeSum1([5,1,5,5,2,5,4]))#True
# print(sol.threeSum1([[1,2,2,1]]))#False
