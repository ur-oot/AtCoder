import math

X = int(input())

if X == 2:
    print(X)
    exit()

for num in range(X, 1000001):
    for i in range(2, math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            break
        if i == math.floor(math.sqrt(num)):
            print(num)
            exit()
