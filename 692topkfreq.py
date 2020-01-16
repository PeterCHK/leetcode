"""
words = ["i", "love", "leetcode", "i", "love", "coding"]
k=4

def topk(words,k):
    b = dict.fromkeys(words,0)
    for i in words:
        b[i] += 1
        c=sorted(b,key=b.get,reverWzse=True)

    return c[:k]

#print(topk(words,k))
print(topk(words,k))
"""

from collections import Counter
lst=['the','day','is','sunny', 'the', 'the','the','sunny','is','is']
k=4
a=Counter(lst)
b=[]
for i in range(k):

    while 'the' in lst:
        lst.remove('the')
    print(lst)

    b.append(max(Counter(lst))
print(b)
