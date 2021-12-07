S = input()

CN = S.count("N")
CW = S.count("W")
CS = S.count("S")
CE = S.count("E")

if (CN == 0 and CS != 0) or (CN != 0 and CS == 0):
    print("No")
elif (CW == 0 and CE != 0) or (CW != 0 and CE == 0):
    print("No")
else:
    print("Yes")
