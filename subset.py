def subsets(nums):
    n = len(nums)
    output = [[]]

    for num in nums:
        output += [curr + [num] for curr in output]

    return output[1:]

#List=[1,2,3,4,5]
nums=[1,2,3,4,5]

print(subsets(nums))
