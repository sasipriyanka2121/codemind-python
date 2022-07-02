n = int(input())
l = list(map(int,input().split(' ')))
p = int(input())
if p>len(l):
    p = int(p%len(l))
l = (l[-p:] + l[:-p])
for i in l:
    print(i,end=' ')