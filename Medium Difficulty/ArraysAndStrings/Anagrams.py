class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        words_per_respresentaion = dict()

        for word in strs:
            repr = self.getBinaryRepresentationStringForWord(word)
            if repr in words_per_respresentaion:
                words_per_respresentaion[repr].append(word)
            else:
                words_per_respresentaion[repr] = [word]
        return list(words_per_respresentaion.values())

    def getBinaryRepresentationStringForWord(self,s):
        binaryList = [0]*26
        size = len(s)
        a_pos = ord('a')
        for i in range(size):
            index = ord(s[i]) - a_pos
            binaryList[index] += 1

        stringRes = ""

        for val in binaryList:
            stringRes += str(val) + ","
        return stringRes[:-1]

sol = Solution()

print(sol.groupAnagrams( ["bdddddddddd","bbbbbbbbbbc"]))

