N = int(input())
X = list(map(int, input().split()))

hp = (100**2)*N

for i in range(101):
    tmphp = 0
    for j in X:
        tmphp += (i - j) ** 2
    if tmphp < hp:
        hp = tmphp

print(hp)
