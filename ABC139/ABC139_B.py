A, B = map(int, input().split())

sum = 1
num = 0

while B > sum:
    sum += A - 1
    num += 1

print(num)
