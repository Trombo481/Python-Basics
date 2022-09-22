x=int(input("A number please...."))
reverse_num=0
temp=x
while x!=0:
    digit_2=x%10
    reverse_num=reverse_num*10+digit_2
    x//=10
#Answer:-
print("Reverse=",reverse_num)
if temp==reverse_num:
    print("<<THIS IS A PALINDROME NO.>>")
else:
    print("<<THIS NO. IS NOT A PALINDROME.>>")
