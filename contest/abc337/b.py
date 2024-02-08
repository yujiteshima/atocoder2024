#S = list(input())
#S = sorted(set(S), key=S.index)

#ans = "".join(S)
#if ans == "A" or ans == "B" or ans == "C" or ans == "AB" or ans == "BC" or ans == "AC" or ans == "ABC":
#    print("Yes")
#else:
#    print("No")

from collections import Counter

S = input()

C = Counter(S)
T = 'A' * C['A'] + 'B' * C['B'] + 'C' * C['C']

if S == T:
    print("Yes")
else:
    print("No")
