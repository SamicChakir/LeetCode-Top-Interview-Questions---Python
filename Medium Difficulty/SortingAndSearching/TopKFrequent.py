class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        occs = self.getOccurences(nums)

        numberWithCertainOccs = self.getNumbersWithCertainOccs(occs)

        #should code your own sorting function Onlogn , will use merge sort
        sortedkeys = sorted(numberWithCertainOccs.keys())
        sizeSortedKeys = len(sortedkeys)
        res = []
        count = 0

        current = -1
        while current >= -sizeSortedKeys:
            currentOcc = sortedkeys[current]
            currentNumbers = numberWithCertainOccs[currentOcc]
            i = 0
            while ( i < len(currentNumbers)):
                res += [currentNumbers[i]]
                if len(res) == k:
                    return res
                i += 1
            current -= 1
        return res


    def getNumbersWithCertainOccs(self,occs):

        NumbersWithCertainOccs = dict()

        for num in occs.keys():
            if occs[num] in NumbersWithCertainOccs:
                NumbersWithCertainOccs[occs[num]].append(num)
            else:
                NumbersWithCertainOccs[occs[num]] = [num]

        return NumbersWithCertainOccs


    def getOccurences(self, nums):
        occs = dict()
        for num in nums:
            if num in occs:
                occs[num] += 1
            else:
                occs[num] = 1

        return occs



sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3],2))