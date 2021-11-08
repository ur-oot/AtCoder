S = input()

st0 = ''
st1 = ''

for i in range(len(S)):
    if i % 2 == 0:
        st0 += '0'
        st1 += '1'
    else:
        st0 += '1'
        st1 += '0'

cst0 = bin(int(st0, 2) ^ int(S, 2)).count('1')
cst1 = bin(int(st1, 2) ^ int(S, 2)).count('1')

print(min(cst0, cst1))
