"""
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = set()


    def insert(self, val: int) -> bool:
        if val not in self.val:
            self.val.add(val)
            return True
        else:
            return False

        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.val:
            return False
        else:
            self.val.remove(val)
            return True


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        a = self.val.pop()
        self.val.add(a)
        return a

"""
import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if not val in self.data:
            self.data[val]=1
            return True
        return False


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.data:
            del self.data[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        keys = list(self.data.keys())
        return random.choice(keys)
# Your RandomizedSet object will be instantiated and called as such:

obj = RandomizedSet()
val = 1
print(obj.insert(val))
val = 2
print(obj.insert(val))
print(obj.getRandom())
print(obj.remove(val))
print(obj.remove(val))
print(obj.getRandom())
