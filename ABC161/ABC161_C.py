N, K = map(int, input().split())

x = N % K

while True:
    if x > abs(x - K):
        x = abs(x - K)
    else:
        break

print(x)
