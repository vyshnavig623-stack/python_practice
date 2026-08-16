n=int(input("enter a number:"))
largest=n%10
smallest=n%10
while n>0:
    digit=n%10
    if digit>largest:
        largest=digit
    if digit<smallest:
        smallest=digit
    n=n//10
print("largest digit is", largest)
print("smallest digit is", smallest)