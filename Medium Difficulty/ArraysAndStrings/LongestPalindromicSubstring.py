class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        index_of_size3_palindromes = self.getPotentielOddPalindromeMiddlePoints(s)

        index_of_size2_palindromes = self.getPotentielPairPalindromeMiddlePoints(s)

        if ( len(index_of_size2_palindromes) == 0 and len(index_of_size3_palindromes) == 0):
            return s[0]
        size = len(s)
        s_index,e_index = 0, -1

        for (i,j) in index_of_size2_palindromes:
            if ( j - i > e_index - s_index):
                s_index, e_index = i, j
            start,end = i-1,j+1

            while  start >=0  and end < size and s[start] == s[end]:
                if ( end - start  > e_index - s_index):
                        s_index, e_index = start  , end
                start -= 1
                end += 1

        for (i,j) in index_of_size3_palindromes:
            if ( j - i > e_index - s_index):
                s_index, e_index = i, j
            start,end = i-1,j+1

            while start >= 0 and end < size and s[start] == s[end]:
                if (end - start > e_index - s_index):
                    s_index, e_index = start, end
                start -= 1
                end += 1

        if e_index == -1:
            if  len(index_of_size2_palindromes) == 0:
                return s[index_of_size3_palindromes[0][0]:index_of_size3_palindromes[0][1]+1]
            elif  len(index_of_size3_palindromes) == 0:

                return s[index_of_size2_palindromes[0][0]:index_of_size2_palindromes[0][1] + 1]

        return s[s_index:e_index+1]







    def getPotentielOddPalindromeMiddlePoints(self,s):


        index_of_size3_palindrom = []
        size = len(s)

        for i in range(size):
            if i != 0 and i != size - 1 and s[i-1] == s[i+1]:
                index_of_size3_palindrom.append((i-1,i+1))

        return index_of_size3_palindrom

    def getPotentielPairPalindromeMiddlePoints(self, s):
        # at least 4 eleme

        indexofsize2palindrome = []

        size = len(s)

        for i in range(0,size - 1):
            if (s[i] == s[i+1]):
                indexofsize2palindrome.append((i,i+1))


        return indexofsize2palindrome



sol = Solution()

print(sol.longestPalindrome("xaabacxcabaaxcabaax"))
#"xaabacxcabaax"