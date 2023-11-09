class RandomizedSet:

    def __init__(self):
        self.randomizedSet = []

    def insert(self, val: int) -> bool:
        if val in self.randomizedSet:
            return False
        else:
            self.randomizedSet.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.randomizedSet:
            self.randomizedSet.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return self.randomizedSet[randint(0, len(self.randomizedSet) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()