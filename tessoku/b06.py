N = int(input())
A = list(map(int, input().split()))
Q = int(input())

accum = [0] * N
accum[0] = 0;
for i in range(1, N):
    accum[i] = accum[i - 1] + A[i]

for i in range(Q):
    L, R = map(int, input().split())
    L -= 1
    R -= 1
    times = R - (L - 1)
    hit = accum[R] - (accum[L - 1] if L > 0 else 0)
    lose = times - hit
    if hit - lose > 0:
        print("win")
    elif hit - lose == 0:
        print("draw")
    else:
        print("lose")
