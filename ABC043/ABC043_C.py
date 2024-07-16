import math

N = int(input())
A = list(map(int, input().split()))

avg = round(sum(A) / len(A))
result = 0

for an in A:
    result += math.floor(pow((an - avg), 2))

print(result)
