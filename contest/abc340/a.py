A, B, C = map(int, input().split())

ans =[]
ans.append(A)
idx = 0
while True:
   # print(ans[idx])
    if ans[idx] == B:
        break
    ans.append(ans[idx] + C)
    idx += 1

print(*ans)

    

