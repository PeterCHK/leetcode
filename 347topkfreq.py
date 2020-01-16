import statistics
import collections
import heapq


"""
def topKFrequent(nums, k):
    a = []
    for i in range(k):
        b = statistics.mode(nums)
        a.append(b)
        while b in nums:
            nums.remove(b)
"""
def topKFrequent(nums, k):
    count = collections.Counter(nums)
    return sorted(count, key=count.get)[:k]


nums=[1,1,1,1,2,2,2,2,2,3,3,4]
k=2
print(topKFrequent(nums,k))
