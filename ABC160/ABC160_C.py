K, N = map(int, input().split())
A = list(map(int, input().split()))

d = []
for i in range(len(A)):
    if i + 1 == len(A):
        d.append((K + A[0]) - A[i])
    else:
        d.append(A[i + 1] - A[i])

print(K - max(d))
