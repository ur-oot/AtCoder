N, A, B = map(int, input().split())
S = input()

dome = 0
over = 0

for stu in S:
    if "a" == stu:
        if dome + over < A + B:
            dome += 1
            print("Yes")
        else:
            print("No")
    elif "b" == stu:
        if dome + over < A + B and over + 1 <= B:
            over += 1
            print("Yes")
        else:
            print("No")
    else:
        print("No")
