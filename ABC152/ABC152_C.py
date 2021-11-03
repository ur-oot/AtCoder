N = int(input())
P = list(map(int, input().split()))

ans = 0
minP = P[0]

for i in range(N):
    if P[i] <= minP:
        ans += 1
        minP = P[i]

print(ans)
