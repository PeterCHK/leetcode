n=10
nonprime =[]
for i in range(1,int(n/2)+1):
    for x in range(i*2,n,i):
        nonprime.append(x)

print(nonprime)
