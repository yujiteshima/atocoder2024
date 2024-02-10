Q = int(input())
query =[]
for i in range(Q):
    a, b = map(int, input().split())
    if(a == 1):
        query.append(b)
    else:
        print(query[-b])
