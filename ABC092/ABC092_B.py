N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

c = 0

for an in A:
    i = 0
    while D >= (an * i) + 1:
        c += 1
        i += 1

print(c + X)
