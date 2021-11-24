A, B, K = map(int, input().split())

for i in range(A, min(B, A + K - 1) + 1):
    print(i)

for i in range(max(B - K + 1, A + K), B + 1):
    print(i)
