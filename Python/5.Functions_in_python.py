#calling a functions
def my_function():
    a=str(input("What is your name?"))
    if a=="Tmbk":
        print("Hello")
    else:
        print("Bye")
print("xyz")
my_function()

#Arguments and parameters
def my_sum(n1,n2):
    sum=n1+n2
    if sum<=100:
        print("Small sum")
    else:
        print("Big Sum")
    return sum
print("Fnc. is going to run....")
x=my_sum(12,90)
y=my_sum(100,200)
result=x*y
print(result)

#LIST ARGUMENTS
def my_new(*n1):
    sum=n1[1]+n1[2]
    if sum<=100:
        print("Small sum")
    else:
        print("Big Sum")
    return sum
print("1...2...3...go...")
print(my_new(12,100,200,90))

#DICTIONARY ARGUMENTS
def new(**k):
    print("Name="+k["N1"])
new(N1="Trombokendu",N2="Biswajit Sir")

#DEFAULT PARAMETERS
def athe_fnc(c="Namaskaram"):
    print(c)
athe_fnc("Illa")
athe_fnc()

#PASSING LIST
def hello_fnc(f):
    for x in f:
        print(x)
fr=["xml","java","python"]
hello_fnc(fr)


#RETURN 
def a_super(x):
    return 5*x
print(a_super(55))

#PASSING A FUNCTION
def myfnc():
    pass

#RECURSION
def rec(k):
    if k>0:
        result=k+rec(k-1)
        print(result)
    else:
        result=0
    return result
print(rec(6))
