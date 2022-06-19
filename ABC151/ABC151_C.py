N, M = map(int, input().split())

list = []
for i in range(M):
    p, S = input().split()
    list.append([int(p), S])

countWA = [0] * N
countAC = [0] * N
for v in list:
    if countAC[v[0] - 1] == 0:
        if v[1] == "WA":
            countWA[v[0] - 1] += 1
        else:
            countAC[v[0] - 1] = 1

sumCountWA = 0
for i in range(N):
    if countAC[i] == 1:
        sumCountWA += countWA[i]

print(sum(countAC), sumCountWA)
