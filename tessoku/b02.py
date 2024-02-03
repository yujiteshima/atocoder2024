A, B = map(int, input().split())
found = False
for i in range(A,B+1):
    if( 100 % i == 0):
        found = True
print("Yes" if found else "No")
