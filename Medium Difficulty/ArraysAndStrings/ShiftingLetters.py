class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        s_size = len(s)
        a_pos = ord('a')

        cumulated_shifts = self.cumulated_sum_array(shifts, s_size)

        integer_per_letter = [ord(s[i]) - a_pos for i in range(s_size)]

        shifted_s = []

        for i in range(s_size):
            shifted_number = cumulated_shifts[i] + integer_per_letter[i]

            shifted_s += [chr(shifted_number % 26 + a_pos)]

        return ''.join(shifted_s)

    def cumulated_sum_array(self, array, size):

        cumulated_sum = []
        current_sum = 0

        for i in reversed(range(size)):
            current_sum += array[i]
            cumulated_sum.insert(0, current_sum)
        return cumulated_sum


sol = Solution()
print(sol.shiftingLetters("abc", [3,5,9]))