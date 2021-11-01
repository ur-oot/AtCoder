S = input()

for i in range(97, 123):
    if S.find(chr(i)) == -1:
        print(chr(i))
        exit()

print("None")
