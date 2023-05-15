a = input().split()
a1= set()
for i in a:
    if i in a1:
        print('YES')
    else:
        print('NO')
    a1.add(i)