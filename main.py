
from collections import Counter

num_shoes = int(input())

size = input().split()

sizeList = []
for s in size:
    sizeList.append(s)

stock = Counter(sizeList)

num_customers = int(input())

shoe_size = []
shoe_price = []
for _ in range(num_customers):
    size_price = input().split()
    shoe_size.append(size_price[0])
    shoe_price.append(int(size_price[1]))

output = 0
for i in range(num_customers):
    s = shoe_size[i]
    if stock[s] > 0:
        output += shoe_price[i]
        stock[s] -= 1

print(output)
