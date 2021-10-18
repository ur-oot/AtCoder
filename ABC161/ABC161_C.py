N, K = map(int, input().split())

ans = min(K - (N % K), N % K)

print(ans)
