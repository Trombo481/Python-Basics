
list_inp= []
for i in range (0,8):
    e=int(input("GIVE 8 NUMBERS FOR YOUR PASSWORD. "))
    list_inp.append(e)

print("THE NUMBERS YOU GAVE ARE:",list_inp)


def randomboy():
    import random
    randomlist=[]
    for i in range (list_inp):
        n=random.randint(1,30)
        randomlist.append(n)
    print()