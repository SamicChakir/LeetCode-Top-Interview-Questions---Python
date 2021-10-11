class Solution:
    def calculate(self, s):
        return self.executePlusMinusOperations(self.removeMultiplicationAndDivision(self.transformToList(s)))

    def removeMultiplicationAndDivision(self,list_operations):

        new_list = []
        size = len(list_operations)
        i = 0
        while(i < size):
            if list_operations[i] == "*":
                resOp = new_list[-1] * list_operations[i+1]
                new_list[-1] = resOp
                i = i +2
            elif list_operations[i] == "/":
                resOp = int(new_list[-1] / list_operations[i + 1])
                new_list[-1] = resOp
                i += 2
            else:
                new_list.append(list_operations[i])
                i += 1

        return new_list

    def executePlusMinusOperations(self,list_operations):
        if len(list_operations) == 1:
            return list_operations[0]
        sum = 0
        size = len(list_operations)
        new_list = [0]
        i = 0
        while(i < size):
            if list_operations[i] == "+":
                sum += list_operations[i + 1]
                i = i + 2
            elif list_operations[i] == "-":
                sum += - list_operations[i+1]
                i = i + 2
            else:
                sum += list_operations[i]
                i = i + 1
        return sum


    def transformToList(self,s):
        size = len(s)
        curInt = ""
        list_repr = []
        for i in range(size):
            if s[i] == "*":
                list_repr.append(int(curInt))
                list_repr.append("*")
                curInt = ""

            elif s[i] == "/":
                list_repr.append(int(curInt))
                list_repr.append("/")
                curInt = ""
            elif s[i] == "+":
                list_repr.append(int(curInt))
                list_repr.append("+")
                curInt = ""
            elif s[i] == "-":
                list_repr.append(int(curInt))
                list_repr.append("-")
                curInt = ""
            elif s[i] == " ":
                continue
            else:
                curInt += s[i]
        list_repr.append(int(curInt))
        return list_repr


sol = Solution()
print(sol.calculate("3+2*2"))
