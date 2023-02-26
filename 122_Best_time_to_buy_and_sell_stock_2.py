prices = [1]
if len(prices)<=1:
    result = False
for i in range(len(prices)-1):
    if prices[i]>=prices[i+1]:
        result = True
    else:
        result = False
print(result)