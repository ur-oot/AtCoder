S = input()
DE = ["dreamer", "eraser", "dream", "erase"]

T = ""
while True:
    for i, str in enumerate(DE):
        if S.endswith(str + T):
            T = str + T
            if S == T:
                print("YES")
                exit()
            break
        if i == len(DE) - 1:
            print("NO")
            exit()
