# list
list0 = ["muhammad" , 6 ,83.3 , "karachi"] 
str0 = "hellow"
print(str0[0])
# str0[3] = "y"
#give error becouse in python "strings" is immutable, it is not allow to change

# slicing list
print(list0[2: 3])#slicing()
print(list0[:2])#slicing(2and 3)
print(list0[2:])#slicing(2and 3)
# negetive list
print(list0[-3 : -1])#slicing(2and 3)

# tuple
tpl = (1 , 2,3.4 , 4 , 2 , 4, 45 , 56, 4)
print(tpl, type(tpl))
# slicing
print(tpl[2 : 4])
print(tpl.index(2))#to find index of nmbewr
print(tpl.count(2))

#practice question
mylist0 =[ ]
userinput0 = input("enter your 1st favourite mivie: \t")
userinput1 = input("enter your 2st favourite mivie\t ")
userinput2 = input("enter your 3st favourite mivie:\t")
mylist0.append(userinput0)
mylist0.append(userinput1)
mylist0.append(userinput2)
print(mylist0)

# practice question 
lists0 = ["a " , "b" "c"]

list0_copy=lists0.copy()
list0_reverse = list0_copy.reverse()
if(lists0 == list0_reverse):
    print("palindrom")
else:
    print("not a palindrom")

# practice
mylist1 = (" A" , "D ", "B" , "C" ," A  ", "D" , "A")
print(mylist1.count("A"))
list1 = [" A" , "D ", "B" , "C" ," A  ", "D" , "A"]
list1.sort()
print(list1)