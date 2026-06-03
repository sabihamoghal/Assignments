n=int(input("enter anumber:"))
fact=1
if n<0:
    print("factorial can not be performed to negative numbers")
elif n==0:
    print(f'The factorial of {num} is 1')
else:
    for i in range(1,n+1):
        fact=fact*i
    print(f'The factorial of {n} is {fact}')
