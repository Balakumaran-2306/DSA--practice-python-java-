def armstrong_num(n):
    temp=n
    digits=len(str(n))
    result=0
    while n>0:
        rem=n%10
        result=result+(rem**digits)
        n=n//10
    return result==temp
num=int(input('enter a number:'))
if armstrong_num(num):
    print(f"{num} is an armstrong number")
else:
    print(f"{num} is not an armstrong number")
