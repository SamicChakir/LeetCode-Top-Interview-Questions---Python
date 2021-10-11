class Solution:
    def productExceptSelf(self, nums):
        size = len(nums)
        if size == 2:
            return nums

        left_to_right_prod = [nums[0]]
        right_to_left_prod = [nums[size - 1]]
        answer = []
        for i in range(1, size):
            left_to_right_prod.append(left_to_right_prod[-1] * nums[i])
            right_to_left_prod = [right_to_left_prod[0] * nums[size - i - 1]] + right_to_left_prod

        answer.append(right_to_left_prod[1])
        for j in range(1, size - 1):
            answer.append(left_to_right_prod[j - 1] * right_to_left_prod[j + 1])

        answer.append(left_to_right_prod[-2])

        return answer


sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))