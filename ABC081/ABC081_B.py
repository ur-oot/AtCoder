num = input()
int_arr = list(map(int, input().split()))

count = 0

while True:
    for item in int_arr:
        if item % 2 != 0:
            break
    else:
        int_arr = [int(i/2) for i in int_arr]
        count += 1
        continue
    print(count)
    break
