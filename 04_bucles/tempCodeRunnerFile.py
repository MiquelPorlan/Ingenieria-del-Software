resistencies = [100, 220, 470, 1000]
I=[]
for R in resistencies:
    I.append(12/R)
print(I)    