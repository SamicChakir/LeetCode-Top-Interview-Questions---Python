class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        if size <= 1:
            return size

        start_bool_per_letter = self.getBooleanPerLetterDictionary(s)
        current_substringBoolPerLetter = start_bool_per_letter
        current_index_per_letter = dict()

        i = 0
        start_index, end_index = 0, -1
        current_s_index, current_end_index = 0, 0
        alwaysDifferent = True
        while i < size:
            if not current_substringBoolPerLetter[s[i]]: #character not already found in substring
                current_substringBoolPerLetter[s[i]] = True
                current_index_per_letter[s[i]] = i
                current_end_index = i
            else:
                # from current_s_index to i - 1 we have found a substring with no reptead chars
                # we need to comapre it with biggest substring so far and store if bigger
                #after that i = current_index_per_letter[s[i]] + 1
                # remove all letter betwen previous and current_index_per_letter[s[i]] + 1 from current_substringBoolPerLetter and current_index_per_letter
                alwaysDifferent = False
                store_position = current_index_per_letter[s[i]]
                current_end_index = i - 1
                if ( current_end_index - current_s_index > end_index - start_index):
                    start_index, end_index = current_s_index, current_end_index
                for j in range(current_s_index,current_index_per_letter[s[i]]+1):
                    if current_substringBoolPerLetter[s[j]]:
                        current_substringBoolPerLetter[s[j]] = False
                        current_index_per_letter.pop(s[j])
                current_substringBoolPerLetter[s[i]] = True
                current_index_per_letter[s[i]] = i
                current_s_index = store_position +1
                current_end_index = i
            i = i + 1
        if alwaysDifferent:
            return size

        if current_end_index - current_s_index > end_index - start_index:
            return current_end_index - current_s_index + 1


        return end_index - start_index + 1

    def getBooleanPerLetterDictionary(self,s):

        bool_per_letter = dict()

        for char in s:
            if char not in bool_per_letter:
                bool_per_letter[char] = False

        return bool_per_letter



sol = Solution()
print(sol.lengthOfLongestSubstring("aab"))