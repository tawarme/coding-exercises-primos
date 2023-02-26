import random

class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if self.indices.get(val) is not None:
            return False

        self.indices[val] = len(self.arr)
        self.arr.append(val)
    
        return True

    def remove(self, val: int) -> bool:
        i_val = self.indices.get(val)

        if i_val is None:
            return False

        last = self.arr[-1]

        self.indices[last] = i_val
        self.arr[i_val] = last
        self.arr[-1] = val

        del self.indices[val]

        self.arr.pop()
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()