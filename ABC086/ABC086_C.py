N = int(input())
tmpt = 0
tmpx = 0
tmpy = 0
for i in range(N):
    t, x, y = map(int, input().split())
    if (abs(x - tmpx) + abs(y - tmpy)) > (t - tmpt) or (
        abs(x - tmpx) + abs(y - tmpy)
    ) % 2 != (t - tmpt) % 2:
        print("No")
        exit()
    tmpt = t
    tmpx = x
    tmpy = y

print("Yes")
