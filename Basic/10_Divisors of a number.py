def divisor_number(n):
    print("divisors are:")
    for i in range(1,n+1):
        if n%i==0:
            print(i,end=" ")
n=int(input("Enter a number:"))
divisor_number(n)
