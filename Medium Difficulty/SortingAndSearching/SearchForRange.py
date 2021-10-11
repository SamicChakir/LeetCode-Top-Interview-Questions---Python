class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size = len(nums)
        if size == 0:
            return [-1,-1]
        if target > nums[-1]:
            return [-1,-1]
        if target < nums[0]:
            return [-1,-1]


        return self.searchRangeRec(nums,0,size-1,target)

    def searchRangeRec(self,nums,start,end,target):
        if start < end:
            size = end - start + 1
            if target > nums[end]:
                return [-1, -1]
            if target < nums[start]:
                return [-1, -1]


            middle = start + size // 2
            val_middle = nums[middle]
            if val_middle < target:
                #search in middle+1:
                return self.searchRangeRec(nums,middle+1,end,target)
            elif val_middle > target:
                #search in 0:middle-1
                return self.searchRangeRec(nums,start,middle-1,target)
            else:
                #found value look right and left for lower and upper boundaries
                leftPart = self.searchRangeRec(nums,start,middle-1,target)
                if max(leftPart) == -1:
                    leftPart = []
                rightPart = self.searchRangeRec(nums,middle+1,end,target)
                if max(rightPart) == -1:
                    rightPart = []
                resList = rightPart + leftPart + [middle]
                return [min(resList),max(resList)]

        elif start == end:
            if nums[start] == target:
                return [start,start]
            return [-1,-1]
        return [-1,-1]


sol = Solution()
print(sol.searchRange([],6))