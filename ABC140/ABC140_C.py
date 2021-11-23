N = int(input())
B = list(map(int, input().split()))

A = []
for i in range(1, N - 1):
    A.append(min(B[i - 1], B[i]))

A.insert(0, B[0])
A.append(B[N - 2])

print(sum(A))
