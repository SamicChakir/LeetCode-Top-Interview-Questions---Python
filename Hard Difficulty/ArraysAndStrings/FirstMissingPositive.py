import sys


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min = sys.maxsize
        negatifs = 0
        for num in nums:
            if num <= 0:
                negatifs += 1
            elif num < min:
                min = num
        if min > 1:
            return 1
        nb_positifs = len(nums) - negatifs
        binary_repr = (1 << (nb_positifs) ) + 1 # this is not space complexity ??

        for num in nums:
            if num >= 2 and num <= nb_positifs:
                binary_repr = binary_repr | (1 << (num -1))

        count = 1
        while binary_repr != 1:
            if not binary_repr & 1:
                break
            count += 1
            binary_repr = binary_repr >> 1
        return count



sol = Solution()
print(sol.firstMissingPositive([-1,-2,-60,40,43]))
