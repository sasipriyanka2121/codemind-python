n=int(input())
for i in range(1,n+1):
  i=input()
  c=0
  for t in i:
    if t.isdigit():
        c=c+1
  if c>0:
     print("Yes")
  else:
     print("No")