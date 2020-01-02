#input=2,3,4,5,6
#output=2,3,5,8,13

def climbStairs(n):
    if n==2:
        return 2
    if n==3:
        return 3
    return climbStairs(n-1) + climbStairs(n-2)

print(climbStairs(6))
