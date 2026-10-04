import random
class RandomizedSet:

    def __init__(self):
      self.values = []
      self.index_map = {}

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False

        index = len(self.values)

        self.values.append(val)
        self.index_map[val] = index

        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False

        remove_index = self.index_map[val]
        last_val = self.values[-1]

        self.values[remove_index] = last_val
        self.index_map[last_val] = remove_index

        self.values.pop()
        del self.index_map[val]

        return True
      
    def getRandom(self) -> int:
        return random.choice(self.values)