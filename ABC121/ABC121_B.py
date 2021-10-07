N, M, C = map(int, input().split())
B = list(map(int, input().split()))

count = 0

for j in range(N):
    tmp = 0
    A = list(map(int, input().split()))
    for i in range(M):
        tmp += A[i] * B[i]
    if tmp + C > 0:
        count += 1

print(count)
