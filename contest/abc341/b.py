N = int(input())
A = list(map(int, input().split()))

for i in range(N-1):
    s, t = map(int, input().split())
    c = A[i] // s
    A[i+1] += c * t

print(A[N-1])

