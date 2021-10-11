class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        size = len(nums)
        if size == 0:
            return -1
        elif size == 1:
            if nums[0] == target:
                return 0
            return -1
        elif size == 2:
            if nums[0] == target:
                return 0
            if nums[1] == target:
                return 1
            return -1
        pivot = 0
        if nums[0] > nums[1]:
            pivot = 1

        elif nums[size-2] > nums[size-1]:
            pivot = size - 1
        else:
            pivot = self.getPivotIndex(nums,1,len(nums)-2)

        cuttedArray = nums[pivot:] + nums[:pivot]
        position = self.binarySearchArray(cuttedArray,0,len(cuttedArray)-1,target)
        if position == -1:
            return position
        return (pivot + position)%size


    def getPivotIndex(self,nums,start_index,end_index):
        size = len(nums)

        while start_index <= end_index:
            middle = (start_index + end_index) // 2
            if nums[middle-1] < nums[middle] and nums[middle] > nums[middle+1]:
                return middle + 1
            elif nums[middle] < nums[0]:
                end_index = middle - 1

            elif nums[middle] > nums[size - 1]:
                start_index = middle +1
            else:
                return 0
        return 0

    def binarySearchArray(self,nums,low,high,val):
        if low <= high:
            middle = (low + high)//2
            if nums[middle] == val:
                return middle
            elif nums[middle] > val:
                return self.binarySearchArray(nums, low, middle - 1, val)
            else:
                return self.binarySearchArray(nums, middle + 1, high, val)
        return -1


sol = Solution()
print(sol.search([4,5,6,7,0,1,2], 0))