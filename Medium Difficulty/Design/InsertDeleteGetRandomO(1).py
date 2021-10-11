import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set_of_vals = set()
        self.ListOfVals = list()
        self.positionPerVal = dict()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.set_of_vals:
            return False
        self.set_of_vals.add(val)
        self.ListOfVals.append(val)
        self.positionPerVal[val] = len(self.ListOfVals) - 1
        return True


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.set_of_vals:
            self.set_of_vals.remove(val)
            val_position = self.positionPerVal[val]
            last_index_val = self.ListOfVals[-1]
            self.ListOfVals[-1],self.ListOfVals[val_position] = val,last_index_val
            self.positionPerVal[last_index_val] = val_position
            del self.positionPerVal[val]
            self.ListOfVals.pop()

            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        randomNumber = int(random.uniform(0,len(self.ListOfVals)-0.5))
        return self.ListOfVals[randomNumber]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


sol = RandomizedSet()

print(sol.insert(0))
print(sol.insert(1))
print(sol.insert(2))

print(sol.getRandom())
print(sol.getRandom())
print(sol.getRandom())
print(sol.getRandom())
print(sol.getRandom())
print(sol.getRandom())

print(sol.getRandom())
print(sol.getRandom())
print(sol.getRandom())
print(sol.getRandom())
print(sol.getRandom())
print(sol.getRandom())

print(sol.getRandom())
print(sol.getRandom())
print(sol.getRandom())
print(sol.getRandom())
print(sol.getRandom())
print(sol.getRandom())

print(sol.getRandom())
print(sol.getRandom())
print(sol.getRandom())
print(sol.getRandom())
print(sol.getRandom())
print(sol.getRandom())

