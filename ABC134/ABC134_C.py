N = int(input())
A = [int(input()) for _ in range(N)]

tmpA = sorted(A)

M1 = tmpA[-1]
M2 = tmpA[-2]
for i in A:
    if M1 != i:
        print(M1)
    else:
        print(M2)
