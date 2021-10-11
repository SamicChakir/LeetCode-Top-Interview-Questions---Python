from decimal import *

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        getcontext().prec = 400
        fraction = Decimal(numerator) / Decimal(denominator)
        comma_position = 0
        str_representation = str(fraction)
        size = len(str_representation)
        comma_present = False
        for l in range(size):
            if str_representation[l] == ".":
                comma_position = l
                comma_present = True
                break
        if not comma_present:
            return str_representation


        splited_string = str_representation.split("E")

        if len(splited_string) == 2:
            numberOfZeros = int(splited_string[-1][1:])
            splited_string2 = str_representation.split(".")
            str_representation = "0." + "0"*(numberOfZeros-1) + splited_string2[0] + splited_string2[1]

        alreadySeen = dict()
        new_str = ""

        for i in range(size):
            if str_representation[i] in alreadySeen:
                if i == size - 1:
                    break
                position = alreadySeen[str_representation[i]]
                potentiel_sequence = new_str[position:]
                size_seq = len(potentiel_sequence)
                loopable_str = str_representation[i:]
                valableSeq = True
                count = 0
                j = 0
                original_suiv = str_representation[position + 1]
                current_suiv = str_representation[i+1]
                if current_suiv != original_suiv:
                   valableSeq = False

                if valableSeq:
                    new_str += ")"
                    new_str = new_str[:position] + "(" + new_str[position:]
                    break
            else:
                alreadySeen[str_representation[i]] = i
            new_str += str_representation[i]
            if str_representation[i] == ".":
                comma_position = i
                alreadySeen = dict()

        return new_str


sol = Solution()
print(sol.fractionToDecimal(1,214748364))