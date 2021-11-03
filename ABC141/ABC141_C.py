N, K, Q = map(int, input().split())
A = [int(input()) for i in range(Q)]

P = [K - Q for _ in range(N)]

for i in A:
    P[i - 1] += 1

for j in P:
    if j > 0:
        print("Yes")
    else:
        print("No")
