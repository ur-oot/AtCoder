N = int(input())
SN = []
for _ in range(N):
    s, n = input().split()
    SN.append((s.strip(), int(n)))

res = sorted(SN, key=lambda SN: (SN[0], -SN[1]))

for i in res:
    print(SN.index(i) + 1)
