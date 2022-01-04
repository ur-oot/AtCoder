N, L = map(int, input().split())
SN = [input() for _ in range(N)]

ans = ""

for str in sorted(SN):
    ans += str
print(ans)
