#s = "anagram", t = "nagaram" true
#s = "rat", t = "car" false
"""
from collections import Counter


s2 = Counter(s)
t2 = Counter(t)

print(s2 - t2 == t2-s2 == Counter())
"""
s = "anagram"
t = "nagarasm"
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

print(isAnagram(s,t))
