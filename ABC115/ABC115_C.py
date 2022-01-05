N, K = map(int, input().split())
HN = [int(input()) for _ in range(N)]

ans = 10 ** 9

HN = sorted(HN)
for i in range(N - K + 1):
    ans = min(ans, HN[i + K - 1] - HN[i])

print(ans)
