print("hellow")
print("I am Rimsha Parveen")

# data types
name = "rimsha parveen"
age= 19
employee = ''
qualification = True
print(type(name))
print(type(age))
print(type(employee))
print(type(qualification))

# operaotrs
num1 = 273
num2 = 9
sum = num1 + num2
print("arthimetics operator")
print("a+b = \t" , sum)
print("a - b = \t" , num1 -  num2)
print("a * b = \t " , num2 * num1)
print("a / b = \t " , num1 / num2)
print("a (module) b = \t ", num1 % num2)
print("a**=\n" , num2**num1)

# comment
print("there is two type of comment  \n 1 : single line comments (#......)\n 2 : multi comment  (*** .......***)" )

print("relatinal operator / camparision operator")
# it give boolian value
print(num1 == num2)#false
print(num1 >= num2)#true
print(num1 != num2)#true

# assignment operator
num1 = num1-32
num2 += 40#shorcut method num2 = num2 + 40

print(num1)#241
print(num2) #49
num1 *= 0 #shortcut metod
print(num1) # 0


# logical operator AND OR NOT 
# NOT operator give opposit boolin value
a = True
b = False
num = 34
nuM = 38
print( not True)
print( not False)
print( not (num > nuM))#true
print( not (nuM > num))#false

print("or operator" , nuM or num)
num = True
nuM = True
#and operator(both shold tobe true.....true else false)
print( "that's your answer" , num and nuM) # true


#or operator
print("or operator" , nuM or num) #true
num = True
nuM = False
print("that's your answer" , num and nuM)#false

#or operaot ( one shold to true)
print("or operator" , nuM or num)

#conversion
veri = 3.4
veri1 = 76
print(veri + veri1)
ver  = "rimsha parveen"
print("34",  ver)
myint = 25
mystr = "rimsha parveen"
myflt = 35.76
myflt1 =int(myflt)
print(myflt1+ 35)
# print(int(mystr) , type(mystr))#error
# print( myflt + myint)#error
cng = int(myflt)
print(type(cng))
# print( myint + int(myflt))#give error

para  = "hye! this is rimsha parveen 952"
print(para.upper())
print(para.lower())
print(para.capitalize())
print(para.find("s"))

# list
lst=["rimsha parveen" , 19 , 952 ]
print(lst)
print(type(lst))
lst[2] =952 
print(lst[2] + 5)

#tuple
tpl = ("ali" , "ahmed" , "usman" , 8)
print(tpl)
print(type(tpl))
# tpl[2] = "hamza"
# above statement give error becouse tuple does not support to add
print(tpl)

# Dictionary
dict1={}
dict1["nouman"] = 20
dict1["usman"] = 16
print(dict1.keys())
print(dict1.items())
print(type(dict1))
print(dict1.keys())
list1= [1 , 2 , 3, 3 , 4 , 2, 2 ,1]
print(list1)
print(set(list1))
print(type(list1))

x1 = 23
y1 = "26"
# print(x1+ y1)#not possible reason of data type
y1 = float(y1)
print(x1 + y1)
c = "amin alam"
print(c.find("i"))
print(str(x1)+str(y1) + c)

inp = int(input("enter num: \n"))
inp1 = int(input("enter 2nd num"))
print(inp + inp1)
if ( inp == inp1) :
    print("both equal")
elif(inp1> inp1 ):
    print("1st is greator")
else:
    print("1st is lessor")

# practice
input1 = int(input("enter a number  : \t"))
input2 = int(input("enter 2nd number: \t"))
print(input1 + input2)

# 2nd question
input1 = int(input("enter width of s/q: \t"))
print(input1*input1)

# 3rd question
input1 = float(input("enter 1st num: \t"))
input2 = float(input("enter 2nd num:\t"))
print((input1+input2)/2)

# 4th question
input1 = float(input("enter 1st num: \t"))
input2 = float(input("enter 2nd num:\t"))
print(input1>= input2)