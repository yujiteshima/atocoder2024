from collections import deque

N = int(input())
kokuban = deque([])
kokuban.append(N)
ans = 0
while True:
    #print(kokuban)
    if not kokuban:
        break
    a = kokuban.popleft()
    #print(a)
    if a < 2:
        #print("pass")
        continue
    ans += a
    
    b =  a // 2
    c = (a + 2 -1) // 2

    kokuban.append(c)
    kokuban.append(b)

print(ans)
