#4)Print the sum of digits of a given input by the user.
def my_fnc(n):

    sum=0
    return sum
n=int(input("Give a number."))

#Answer:-
print("The sum of the digits of your number is",my_fnc(n))
#OR
x=int(input("A number please...."))
y=0
while x!=0:
    digit_2=x%10
    y=y+digit_2
    x//=10
#Answer:-
print(y)