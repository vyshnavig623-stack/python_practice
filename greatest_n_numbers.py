n=int(input("enter number of elemets:"))
largest=-1
for i in range(1,n+1):
    a=int(input("enter a number:"))
    if(a>largest):
        largest=a
print("largest number :",largest)