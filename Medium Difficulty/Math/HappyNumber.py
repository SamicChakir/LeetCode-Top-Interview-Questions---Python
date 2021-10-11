class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        previous = n
        current = self.getSumdigits(previous)
        alreadyFound = set()
        alreadyFound.add(current)
        alreadyFound.add(previous)

        while(previous != current):
            if current == 1:
                return True
            previous = current
            current = self.getSumdigits(previous)
            if current in alreadyFound:
                return False
            alreadyFound.add(current)
        return False


    def getSumdigits(self,n):
        string_rep = str(n)
        sum_digits = 0

        for char in string_rep:
            sum_digits += int(char)*int(char)

        return sum_digits


sol = Solution()
print(sol.isHappy(19))
print(sol.isHappy(2))