class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return list(self.recursiveParenthesis(n,dict()))

    def recursiveParenthesis(self, n,storedCombis):

        if n == 1:
            return ["()"]

        res = set()
        seenCouples = set()
        previous = set()
        sec_previous = set()
        for i in range(1,n):
            cur_res = set()
            if i == 1:
                if n - 1 not in storedCombis:
                    previous = self.recursiveParenthesis(n - 1,storedCombis)
                    storedCombis[n-1] = previous
                else:
                    previous = storedCombis[n-1]

                for elem in previous:
                    cur_res.add(elem + "()")
                    cur_res.add("()" + elem)
                    cur_res.add("(" + elem + ")")
            else:
                if i in storedCombis:
                    previous = storedCombis[i]
                else:
                    previous = self.recursiveParenthesis(i,storedCombis)
                    storedCombis[i] = previous

                if n - i in storedCombis:
                    sec_previous = storedCombis[n-i]
                else:
                    sec_previous = self.recursiveParenthesis(n-i,storedCombis)
                    storedCombis[n-i] = sec_previous
                for str1 in previous:
                    for str2 in sec_previous:
                        cur_res.add(str1 + str2)
                        cur_res.add(str2 + str1)
            res = set.union(res,cur_res)

        storedCombis[n] = res
        return res



sol = Solution()
res = sol.generateParenthesis(3)
print(res)
print(len(res))
