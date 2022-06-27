l,r,k=map(int,input().split())
c=0
for n in range(l,r+1):
  if n%k==0:
     c+=1
print(c) 