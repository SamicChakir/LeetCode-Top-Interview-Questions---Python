class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size = len(nums)
        if size == 1:
            return True

        MaxReachablePositionPerIndex = self.getMaxReachablePostionsPerIndex(nums)
        indextoReach = size - 1
        i = size - 2
        while i >= 0:
            maxReacheableIndex = MaxReachablePositionPerIndex[i]
            if maxReacheableIndex >= indextoReach:
                indextoReach = i

            i = i - 1
        if indextoReach == 0:
            return True
        return False


    def getMaxReachablePostionsPerIndex(self,nums):
        res = []
        size = len(nums)
        for i in range(size):
            res.append(i+nums[i])
        return res