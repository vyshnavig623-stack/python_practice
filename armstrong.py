n=int(input("enter a number:"))
num=n
sum=0
temp=n
count=0
while temp>0:
    temp=temp//10
    count=count+1
while n>0:
    digit=n%10
    sum=sum+digit**count
    n=n//10
if sum==num:
    print("armstrong number")
else:
    print("not a armstrong number")
