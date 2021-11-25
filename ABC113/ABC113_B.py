N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

dmin = 10**5
h = 0

for i in range(len(H)):
    d = abs(A - (T - H[i] * 0.006))
    if d < dmin:
        dmin = d
        h = i

print(h + 1)
