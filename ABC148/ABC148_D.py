N = int(input())
A = list(map(int, input().split()))

s = 1
for i in range(N):
    if A[i] == s:
        s += 1

if s == 1:
    print("-1")
else:
    print(N - (s - 1))
