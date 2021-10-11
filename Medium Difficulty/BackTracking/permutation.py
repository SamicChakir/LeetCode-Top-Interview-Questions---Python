class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.rec_permute(nums)

    def rec_permute(self,nums):

        if len(nums) == 1:
            return [[nums[0]]]

        if len(nums) == 2:
            return [nums,[ nums[1],nums[0] ]]
        size = len(nums)
        res_of_lists = []
        cur_list = []
        for i in range(size):
            if i == size -1:
                cur_list = nums[:-1]
            else:

                cur_list = nums[:i] + nums[i+1:]

            previous = self.rec_permute(cur_list)
            for j in range(len(previous)):
                previous[j] = [nums[i]] + previous[j]

            res_of_lists += previous

        return res_of_lists


    def insertAtEveryIndex(self,List,number):

        res = []
        size = len(List)

        for i in range(size):
            res.append(List[:i] + [number] + List[i:])

        return res



sol = Solution()

print(sol.permute([1,2,3]))

