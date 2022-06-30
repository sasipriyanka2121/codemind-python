import math
t=int(input())
for i in range(t):
    n=int(input())
    p=math.sqrt(n)
    m=p
    m=int(m)
    if p==m:
        print("True")
    else:
        print("False")