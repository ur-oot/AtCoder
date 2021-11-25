S = input()

if S[0] != "A" or S[2 : len(S) - 1].count("C") != 1:
    print("WA")
    exit()

for s in S.replace("A", "").replace("C", ""):
    if s.isupper():
        print("WA")
        exit()

print("AC")
