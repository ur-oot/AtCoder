import math

M = [int(input()) for _ in range(5)]

RT = []
DT = []
for i in M:
    tmp = math.ceil(i / 10) * 10
    RT.append(tmp)
    DT.append(tmp - i)

print(sum(RT) - max(DT))
