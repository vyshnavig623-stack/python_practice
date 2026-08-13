n=int(input("enter a number:"))
sum=0
temp=n
while n>0:
    digit=n%10
    fact=1
    i=1
    while i<=digit:
        fact=fact*i
        i=i+1
    sum=sum+fact
    n=n//10
if sum==temp:
    print("strong number")
else:
    print("not a strong number")