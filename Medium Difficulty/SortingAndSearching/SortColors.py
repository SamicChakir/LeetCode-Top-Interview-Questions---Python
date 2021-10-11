class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        size = len(nums)

        i = 0
        count = 0
        while i < size - 1:
            count += 1
            if nums[i] <= nums[i+1]:
                i += 1
                continue
            nums[i],nums[i+1] = nums[i+1],nums[i]
            i = max(0,i - 1)
        print("brute force iterations",count)
        return nums

    def sortColorsBis(self,nums):

        size = len(nums)
        if size <= 1:
            return;
        last_available_0_index = -1
        last_available_2_index = size
        i = 0
        count = 0
        while i < size:
            count += 1
            if nums[i] == 0:
                if i > last_available_0_index:
                    nums[i],nums[last_available_0_index+1] = nums[last_available_0_index+1],nums[i]
                    last_available_0_index += 1
                else:
                    i = i +1
            elif nums[i] == 2:
                if i < last_available_2_index:
                    nums[i],nums[last_available_2_index-1] = nums[last_available_2_index-1],nums[i]
                    last_available_2_index -= 1
                else:
                    i = i + 1
            else:
                i = i + 1

        print("iterations",count)

sol = Solution()

array = [1,2,2,2,2,0,0,0,1,1]
print(len(array))
sol.sortColorsBis(array)

print(array)

