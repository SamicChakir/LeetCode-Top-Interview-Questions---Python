class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        size = len(digits)
        if size == 0:
            return []

        letters_per_num = self.getDictinaryLettersPerNum()

        possibilities = letters_per_num[digits[0]]

        for i in range(1,size):
            res_list = []
            letters_per_digit = letters_per_num[digits[i]]
            for letter in letters_per_digit:
                res_list += self.addlettertoAllElements(possibilities,letter)
            possibilities = res_list
        return possibilities


    def addlettertoAllElements(self,listOfWords,letter):
        size = len(listOfWords)
        new_list = []
        for i in range(size):
            new_list.append(listOfWords[i] + letter)
        return new_list



    def getDictinaryLettersPerNum(self):
        letters_per_num = dict()

        letters_per_num['2'] = ["a", "b", "c"]
        letters_per_num['3'] = ["d", "e", "f"]
        letters_per_num['4'] = ["g", "h", "i"]
        letters_per_num['5'] = ["j", "k", "l"]
        letters_per_num['6'] = ["m", "n", "o"]
        letters_per_num['7'] = ["p", "q", "r", "s"]
        letters_per_num['8'] = ["t", "u", "v"]
        letters_per_num['9'] = ["w", "x", "y", "z"]


        return letters_per_num


sol = Solution()

print(sol.letterCombinations("23"))