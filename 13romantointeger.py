symbol=['I','V','X','L','C','D','M']
value=[1,5,10,50,100,500,1000]

roman=dict(zip(symbol,value))
#3999 ->  MMM CM XC IX
#3888 -> MMM DCCC LXXX VIII
#1444 -> M CD XL IV

lst='MMMCMXCIX'
total = 0
for i in range(len(lst)):
    if i>=1 and roman.get(lst[i-1]) < roman.get(lst[i]):
        total += roman.get(lst[i]) - roman.get(lst[i-1])*2
    else:
        total += roman.get(lst[i])
    print(total)
