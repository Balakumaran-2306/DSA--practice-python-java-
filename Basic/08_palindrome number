def palindrome_num(n):
    temp=n
    rev=0
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n//=10
    return rev==temp
num=int(input('enter a number:'))
if palindrome_num(num):
    print(f"{num} is palindrome")
else:
    print(f"{num} is not a palindrome")
