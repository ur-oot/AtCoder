N, M = map(int, input().split())
AB = []

for _ in range(M):
    A, B = map(int, input().split())
    AB.append(A)
    AB.append(B)

for i in range(1, N + 1):
    print(AB.count(i))
