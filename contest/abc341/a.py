N = int(input())
ans = ["1"]
for i in range(2*N):
    if i == 0:
        ans.append("0")
    elif i % 2 == 1:
        ans.append("1")
    else:
        ans.append("0")
ans = "".join(ans)
print(ans)

