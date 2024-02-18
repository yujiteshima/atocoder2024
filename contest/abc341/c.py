H, W, N = map(int, input().split())
T = str(input())
S = [input() for _ in range(H)]


ans = 0

for i in range(1, H - 1):
    for j in range(1, W - 1):
        if S[i][j] == '#':
            break
        for k in range(len(T)):
            x = i
            y = j
            if T[k] == 'L':
                x -= 1
            elif T[k] == 'R':
                x += 1
            elif T[k] == 'U':
                y -= 1
            elif T[k] == 'D':
                y += 1
            if x >= 1 and x <= W - 1 and y >= 1 and y <= H - 1:
                if S[x][y] == '#':
                    break
                print(S[x][y])
        ans += 1
print(ans)
