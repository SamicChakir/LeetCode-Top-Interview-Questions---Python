class Solution:
    def majorityElement(self, nums):

        nums = sorted(nums)
        size = len(nums)
        if size == 1:
            return nums[0]
        middle = size // 2
        i = 0
        while i <= size - 2:
            cur = nums[i]
            suiv = nums[i + 1]
            if cur == suiv:
                count = 2
                j = i + 2
                while j < size:
                    if count >= middle:
                        return cur
                    if nums[j] == cur:
                        count += 1
                    else:
                        break
                    j += 1
                if count >= middle:
                    return cur
            i = i + 1

sol = Solution()
print(sol.majorityElement([2,2,1,1,1,2,2]))