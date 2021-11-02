N, M = map(int, input().split())
L = []
R = []
for i in range(M):
    tmpL, tmpR = map(int, input().split())
    L.append(tmpL)
    R.append(tmpR)

print(max(0, min(R) - max(L) + 1))
