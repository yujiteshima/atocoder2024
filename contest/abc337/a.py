N = int(input())
T = 0
A = 0
for i in range(N):
    t, a = map(int, input().split())
    T += t
    A += a

if T > A :
    print("Takahashi")
elif T == A:
    print("Draw")
else:
    print("Aoki")
