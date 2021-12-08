import collections
from typing import Collection


N = int(input())
S = [input() for _ in range(N)]

s = collections.Counter(S).most_common()

s.sort(key=lambda s: s[0])
s.sort(key=lambda s: s[1], reverse=True)

for key, value in s:
    if s[0][1] == value:
        print(key)
    else:
        exit()
