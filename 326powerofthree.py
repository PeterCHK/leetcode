"""
import math
def isPowerOfThree(n):
    if n == 0 or n==1:
        return False
    return (math.log(n)/math.log(3)).is_integer()
"""
def isPowerOfThree(n):
    while n>1:
        n = n/3
        if n==1:
            return True
    return False


print(isPowerOfThree(6))
