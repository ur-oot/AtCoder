N = int(input())
AN = list(map(int, input().split()))

sum1 = 0
sum2 = 0

for i in range(0, N):
    if i % 2 == 0:
        sum1 += AN.pop(AN.index(max(AN)))
    else:
        sum2 += AN.pop(AN.index(max(AN)))

print(abs(sum1 - sum2))
