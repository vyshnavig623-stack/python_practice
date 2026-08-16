n=int(input("enter a number:"))
count=0
sum=0
while n>0:
    digit=n%10
    if(digit%2==0):
        count=count+1
    else:
        sum=sum+1
    n=n//10
print("count of even digits is", count)
print("count of odd digits is", sum)