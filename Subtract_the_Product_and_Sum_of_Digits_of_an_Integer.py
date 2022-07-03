n=int(input())
product = 1
sum = 0
while n>0:
  rem = n%10
  product = product*rem
  sum = sum+rem
  n=n//10
diff = product-sum
print(diff)