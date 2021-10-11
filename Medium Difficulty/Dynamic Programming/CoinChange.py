import sys.maxsize

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dictio_of_already_counted = dict()
        return self.recursive_coinChange(coins, amount, dictio_of_already_counted)



    def recursive_coinChange(self, coins, amount, alreadyCounted):
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if amount in alreadyCounted:
            return alreadyCounted[amount]
        min_elements = sys.maxsize

        for coin in coins:
            current_val = self.recursive_coinChange(coins,amount-coin,alreadyCounted)
            if current_val >= 0 and current_val < min_elements:
                min_elements = current_val + 1

        if min_elements >= sys.maxsize:
            alreadyCounted[amount] = -1
            return -1
        alreadyCounted[amount] = min_elements
        return min_elements