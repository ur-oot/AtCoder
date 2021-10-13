N = int(input())
K = int(input())
X = list(map(int, input().split()))

d = 0
for i in X:
    d += 2 * i if i < (K - i) else 2 * (K - i)

print(d)
