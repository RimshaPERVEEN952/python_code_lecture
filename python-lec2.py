# type of string 
str0 = "hellow"
str1 = """rimsha parveen"""
str2 ='governour house'

# escape sequence
# \n    ,   \t  , 
# concatination
print(str0+str1)
print(str0[2]+str1)#concatintion
print(str2[2:4])#slicing(2and 3)
str4 = "School"
cng = str4[-4 : -2] #negetive slicing
print(cng)
print(len(str2))

# prctice question
username = (input("enter your name : \t"))
print("user name is : " , username + "\nand name's lengt is" , len(username))

# prctice question
find_dlr = "hellow! thi$ i$ my $nd cla$$"
print(find_dlr.count("$"))

# Conditional statement
age = int(input("enter your age : \t"))
if(age >18):
    print("Can Vote and able for license")
elif(age == 18):
    print(" can vote but you are not able for driving licesne")
else:
    print("you are child")

# pratice question
number0 = 105
number1 = 238
number2 = 121
if( number0 > number1 and number0 > number2):
    print("first number is greater")
elif(  number0  < number1 and number0 < number2):
    print("1st is lessor")
elif(number1 > number0 and number1 > number2):
    print("2nd num is greator")
elif( number1< number1 and number1 < number2):
    print("2nd is lessor")
else:
    print("3rd number is greator")