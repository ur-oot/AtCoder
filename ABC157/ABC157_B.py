A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
B = [int(input()) for _ in range(N)]


def check(x, y):
    res = False
    if A[x][0] == 0 and A[x][1] == 0 and A[x][2] == 0:
        res = True
    if A[0][y] == 0 and A[1][y] == 0 and A[2][y] == 0:
        res = True
    if x == y:
        if A[0][0] == 0 and A[1][1] == 0 and A[2][2] == 0:
            res = True
        if A[2][0] == 0 and A[1][1] == 0 and A[0][2] == 0:
            res = True
    return res

for b in B:
    for i in range(3):
        for j in range(3):
            if b == A[i][j]:
                A[i][j] = 0
                if check(i, j):
                    print("Yes")
                    exit()
                break
        else:
            continue
        break

print("No")
