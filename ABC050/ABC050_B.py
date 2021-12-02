N = int(input())
T = list(map(int, input().split()))
M = int(input())
PX = [(list(map(int, input().split()))) for _ in range(M)]

for i in range(M):
    tmpT = T.copy()
    tmpT[PX[i][0] - 1] = PX[i][1]
    print(sum(tmpT))
