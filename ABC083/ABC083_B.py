N,A,B = map(int,input().split())

s = 0
for i_N in range(1, N+1):
    if A <= sum(list(map(int, str(i_N)))) <= B:
        s += i_N

print(s)
