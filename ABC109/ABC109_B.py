N = int(input())
W = [input() for _ in range(N)]

ans = "Yes"
for i in range(1, N):
    if (W.count(W[i]) >= 2) or (W[i - 1][len(W[i - 1]) - 1] != W[i][0]):
        ans = "No"
        break

print(ans)
