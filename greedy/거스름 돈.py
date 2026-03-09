n = 1260
count = 0

cointypes = [500, 100, 50, 10]

for coin in cointypes:
    count += n // coin
    n %= coin

print(count)


    