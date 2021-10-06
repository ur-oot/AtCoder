A = int(input())
B = int(input())
C = int(input())
X = int(input())

count = 0
for i_A in range(0, A+1):
    for i_B in range(0, B+1):
        for i_C in range(0, C+1):
            if X == (i_A * 500) + (i_B * 100) + (i_C * 50):
                count += 1
print(count)
