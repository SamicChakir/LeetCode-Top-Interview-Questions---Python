class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        Lists = []
        nums = sorted(nums)
        dictio = self.getElementsfromIndexIndict(nums)
        alreadyAddedtriplets = set()
        size = len(nums)
        for i in range(size):
            for j in range(i + 1, size-1):
                currentDictio = dictio[j + 1]
                first = nums[i]
                second = nums[j]
                if -first - second in currentDictio:
                    if (first, second, -first - second) not in alreadyAddedtriplets:
                        Lists += [[first, second, -first - second]]
                        alreadyAddedtriplets.add((first, second,  -first - second))

        return Lists

    def getElementsfromIndexIndict(self, nums):
        dictio = dict()
        size = len(nums)
        for i in range(size):
            for j in range(i+1):
                if j in dictio:
                    dictio[j].add(nums[i])
                else:
                    dictio[j] = {nums[i]}

        return dictio


sol = Solution()

print(sol.threeSum([-1,0,1,2,-1,-4]))