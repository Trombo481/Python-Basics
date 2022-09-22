def patternny_fnc(n):
    for i in range(n):
        for j in range(0,i+1):
            print("(*)","-",")*(","",end="")
        print("\r")

def binary_fnc(n1):
    for i in range(n1):
        for j in range(0,i+1):
            print("0","","1","",end="")
        print("\r")

ask=input("Do you like binary or beautiful patterns? ")
if ask=="Binary":
        binary_fnc(12)
else:
         patternny_fnc(12)       
    
