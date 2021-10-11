class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        count = 1

        for i in range(size):
            start = nums[i]
            current_count = 1
            max_elem = nums[i]
            sequences = [(max_elem,current_count,max_elem)]
            for j in range(i + 1, size):
                current_val = nums[j]
                if current_val <= start:
                    continue
                smallermax_elem = True
                for i in range(len(sequences)):
                    seq_max_elem = sequences[i][0]
                    seq_count = sequences[i][1]
                    seq_prev = sequences[i][2]
                    if current_val > seq_max_elem:
                        smallermax_elem = False
                        sequences[i] = (current_val,seq_count+1,seq_max_elem)
                        if seq_count + 1 > current_count:
                            current_count = seq_count + 1
                    elif current_val > seq_prev:
                        smallermax_elem = False
                        sequences[i] = (current_val, seq_count,seq_prev)

                if smallermax_elem: #current val is necessaryl bigger then start ligne 18
                    sequences.append((current_val,2,start))
                    if 2 > current_count:
                        current_count = 2

            if current_count > count:
                count = current_count
        return count


sol = Solution()
# print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))
# print(sol.lengthOfLIS([0,1,0,3,2,3]))
# print(sol.lengthOfLIS([7,7,7,7,7,7,7]))
# print(sol.lengthOfLIS([0,1,0,8,19,10,11,12,13]))
# print(sol.lengthOfLIS([5,7,-24,12,13,2,3,12,5,6,35]))
# print(sol.lengthOfLIS([5,7,-24,12,13,8,9,10,11]))
print([-64,-86,22,-59,30,-1,58,89,5,62,24,62])