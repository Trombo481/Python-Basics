#creating a new class
class mynew:
    'New Class.'
    x=9
    y=10
    s=x+y
    def myfnc(z,l):
        k=z+l
        return k
    summy=myfnc(9,10)+s
    print(summy)

c1=mynew()

#In-built functions in python
class particle:
    def __init__(self,n,a):
        self.nb=n
        self.ac=a
brisk=particle("xyz",23)
print(brisk.nb)
print(brisk.ac)
print(brisk.nb,"has a particle size of",brisk.ac,"mm")

#Info of 
print("doc=",mynew.__doc__)
print("name=",mynew.__name__)
print("module=",mynew.__module__)
print("base=",mynew.__bases__)
print("dict=",mynew.__dict__)


class brick:
    def __init__(self,m,n):
        self.quantity_pi=n
        self.quality_pi=m
management=brick("OK",100)
management.quality_pi="Best"
print(management.quantity_pi,management.quality_pi)
        