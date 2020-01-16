import random
class Solution:

    def __init__(self, nums):
        self.nums = nums
        self.original = nums
        print(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.original
        return self.original

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        random.shuffle(self.nums)
        return self.nums


# Your Solution object will be instantiated and called as such:
nums = [1,2,3]
obj = Solution(nums)
print(obj.shuffle())
print(obj.reset())
print(obj.shuffle())
