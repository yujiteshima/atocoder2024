N, K = map(int, input().split())

ans = 0

for i in range(1, N+1):
  for j in range(1, N+1):
        w = K - i - j
        if 1 <= w <= N:
            ans += 1

print(ans)
