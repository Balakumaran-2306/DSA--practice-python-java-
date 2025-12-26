def power_of_number(base,exp):
    result=1
    while exp>0:
        result=result*base
        exp=exp-1
    return result
base=int(input("enter a base value:"))
exp=int(input("enter a exp value:"))
answer=power_of_number(base,exp)
print('Result:',answer)
