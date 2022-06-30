def add_digits(n):
    while n>=10:
        temp=0
        while n>0:
            temp=temp+n%10
            n=n//10
        n=temp
    return n
num=int(input())
if(add_digits(num)>=10):
    add_digits(num)
else:
    print(add_digits(num))