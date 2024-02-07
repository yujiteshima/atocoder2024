S = list(input())
rans = []
S.reverse()
for s in S:
    if s == '.':
        break
    rans.append(s)
rans = rans[::-1]
ans = "".join(rans)
print(ans)
