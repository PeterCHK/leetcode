words = ["i", "love", "leetcode", "i", "love", "coding"]
k=4

def topk(words,k):
    b = dict.fromkeys(words,0)
    for i in words:
        b[i] += 1
        c=sorted(b,key=b.get,reverse=True)

    return c[:k]

#print(topk(words,k))
print(topk(words,k))
