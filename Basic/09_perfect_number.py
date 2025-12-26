def is_perfect_number(n):
    if num<=1:
        return False
    total=0
    for i in range(1,n):
        if n%i==0:
           total+=+i
    if total == n:
        return True
    else:
        return False
num=int(input("Enter a number:"))
if is_perfect_number(num):
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")
