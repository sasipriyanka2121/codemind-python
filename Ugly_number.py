def ugly(n):
    if(n==1):
        return 1
    if(n<=0):
        return 0
    if(n%2==0):
        return ugly(n=n//2)
    if(n%3==0):
        return ugly(n=n//3)
    if(n%5==0):
        return ugly(n=n//5)
n=int(input())
if(ugly(n)==1):
    print('Ugly Number')
else:
    print('Not Ugly Number')

