H, W = map(int, input().split())

print("#" * (W + 2))
for _ in range(H):
    print("#{0}#".format(input()))
print("#" * (W + 2))
