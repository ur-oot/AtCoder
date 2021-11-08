N, M = map(int, input().split())

s = []
c = 0
for _ in range(N):
    A = list(map(int, input().split()))
    s += A[1:]

for i in set(s):
    if s.count(i) == N:
        c += 1

print(c)
