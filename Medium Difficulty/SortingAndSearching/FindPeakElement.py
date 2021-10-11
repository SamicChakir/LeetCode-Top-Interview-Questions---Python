class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)

        if size == 1:
            return 0
        if size == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1

        if nums[0] > nums[1]:
            return
            return 0

        if nums[size - 1] > nums[size - 2]:
            return size - 1

        for i in range(1, size - 1):

            if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                return i


sol = Solution()

print(sol.findPeakElement([1,2,3]))