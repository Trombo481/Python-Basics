#Worksheet

#Date: 24/05/2022

#LIST
a_list=[25,50,55,21] #Used in Q.1 and Q.2


#1) Check if the first and last no. of a list is the same:

def check_function():
    if a_list[0]==a_list[3]:
        print("The first and the last no. are the same. ")
    else:
        print("The first and the last no. are not the same. ")

#Answer:-
check_function()

#2)Display the nummbers divisible by 5 from a list 

def divisibility_fnc():
    for i in a_list:
        if i%5==0:
            print(i)
        else:
            print("The number",i,"is not divisible by 5.")

#Answer:-
divisibility_fnc()


#INPUT BUCKET
take_input=int(input("Give me your favourite number.")) #Used in Q.3

#3)Print a number pattern as below:-
        #1
        #2 2
        #3 3 3
        #4 4 4 4
        #5 5 5 5 5

def pattern_fnc():
    num=0
    for i in range(take_input):
        num+=1
        for j in range(0,i+1):
            print(num,"",end="")
        print("\r")

#Answer:-
pattern_fnc()


#Date:28/05/2022

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
print(y)