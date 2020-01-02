import collections
words = ["i", "love", "leetcode", "i", "love", "coding"]
k=4

def topKFrequent(words, k):
    count = collections.Counter(words)
    candidates = count.keys()
    candidates.sort(key = lambda w: (-count[w], w))
    return candidates[:k]

print(topKFrequent(words, k))
