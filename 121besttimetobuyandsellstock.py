#test case 1 [7,1,5,3,6,4]
#leftmin => [7,1,1,1,1,1]
#rightmax => [7,6,6,6,6,4]
#diff => [0,5,5,5,5,3]

#test case 2 [7,2,6,1,5,4]
#leftmin => [7,2,2,1,1,1]
#rightmax => [7,6,6,5,5,4]
#diff => [0,4,4,4,4,3]

prices=[7,1,5,3,6,4]

leftmin=[max(prices)]
rightmax=[min(prices)]
def maxProfit(prices):
    for i in prices:
        if i < min(leftmin):
            leftmin.append(i)
        else:
            leftmin.append(min(leftmin))

    for i in reversed(prices):
        if i > max(rightmax):
            rightmax.append(i)
        else:
            rightmax.append(max(rightmax))
    print(leftmin)
    print(list(reversed(rightmax))-leftmin)
maxProfit(prices)
