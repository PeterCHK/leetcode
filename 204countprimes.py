n=100
nonprime=set()
prime=[]
"""
for i in range(2,int(n/2)+1):
    for x in range(i*2,n+1,i):
        print(i,x)
        nonprime.add(x)

for i in range(2,n+1):
    if i not in nonprime:
        prime.append(i)
print(nonprime,prime)
"""

for i in range(2,n+1):
    if i == 2:
        nonprime.add(i)
    if i >= 3:
        for j in range(2,i-1):
            if i%j==0:
                nonprime.add(i)

prime=set(range(2,n+1))
prime=prime-nonprime
print(prime)
