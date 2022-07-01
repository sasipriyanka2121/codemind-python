n=input()
n1=n.lower()
c=0
x=n1.split()
for i in x:
  if i==i[::-1]:
     c+=1
print(c)     