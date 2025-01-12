# calculator
integer0 = input("enter your expression\t (add ,subtraction, multipliction , division): ")
integer1 = int(input("enter number\t : "))
integer2 = int(input("enter number\t : "))
add = "add"
sub = "subtraction" 
mult = "multiplication" 
div = "division"
if( integer0 == add or integer0  == "+"):
    print("your solution is : \t" , integer1+ integer2)
elif (integer0 == sub or integer0  == "-"):
    print("your solution is : \t" , integer1 - integer2)
elif( integer0 == mult or integer0  == "*"):
    print("your solution is : \t" , integer1* integer2)
elif( integer0 == div or integer0  == "/"):
    print("your solution is : \t" , integer1 / integer2)
else:
    print("you put invalid")
