N = int(input())
A = list(map(int, input().split()))

ans = [0] * N

for i, ai in enumerate(A):
    ans[ai - 1] = i + 1

print(*ans)
