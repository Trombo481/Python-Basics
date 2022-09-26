#LOOP method
n=int(input("Which factorial should be found?"))
fact=1
if n<0:
    print("Your no. is -ve. Sorry we are unable to find factorial.")
elif n==0:
    print("Of course your result is:- factorial of 0=1.")
else:
    print("Fetching.....")
    for i in range(1,n+1):
        fact*=i
    print("Factorial of ",n," is ",fact)

#RECURSION method
def factorial_fnc(n):
    if n==1:
        return 1
    else:
        return (n*factorial_fnc(n-1))
print("Factorial of ",n," is ",factorial_fnc(n))

import math as mt
x=mt.sqrt(6464)
print(x)