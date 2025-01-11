# dictionary
dict1 ={}#null dictionary
print(dict1)
dict1["name"] = "RimshaPrveen"
print(dict1)

# nesting dictionary
students = {
    "name" : "asad",
    "subjects" :{
        "phy" : 23.4,
        "com": 70,
        "math" : 89
        }
}
print(students)
print(students)
print(students["subjects"]["com"])

stu_up = {
    "city" : "karachi",
    "skill":("java" , "javascript" , "python")
}
stu_up0 = {
    "name" : "usman"
}
students.update(stu_up)
students.update(stu_up0)
students.update({"age" : 24})

# set (unordered item)
set1 = { 1 , 2 , 3, 2,"rimsha", "python", 1 , 4  }
print(set1)#duplicate value will ignore
myset = {} # empty set
print(type(myset))
# above is a dictionary not set

set0 = set ()#empty set
set0.add("ali")
set0.add(10)
set0.add("ali834@gmail.com")
set0.add((3, 4 ,5))#but can not add list or dictionary becouse of immutable
print(len(set0))

print(set0)
set0.remove(10)
# set0.clear()#it will clear all data
print(set0.pop())# chose any of random value from set
print(set0.pop())
print(set0)
set0.clear()
print(set0)

# union
my_set1 = { 1 , 3 , 3,5 , 4 , 6 , 10 ,4}
my_set2 = {12 , 4 , 1 , 5 , 14 , 6}
print(my_set1.union(my_set2))#union.....order
print(my_set1.intersection(my_set2))#intersection......same 

# practice  question
# Store following word meanings in a python dictionary
word_meaning = {
    "sun":"source  of light",
    "selfphone" :[ "self use" , "for office"]
}
# You are given a list of subjects for students. Assume one classroom is required for 1
# subject. How many classrooms are needed by all students.

  
subject0 = ("java" , "python ", "javascript" , "c++" , "c ","java" ,"c++","java" ,"python")
print("Total number of class room :\t",len(subject0))
print(type(subject0))

subject = {"java" , "python ", "javascript" , "c++" , "c ","java" ,"c++","java" ,"python"}
print("tataol number of classroom required : \t",len(subject))
print(type(subject))

# practice question
# to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value.

dictionort = {}
x = int(input("enter physice's marks"))
dictionort.update({"phy" : x})

y = int(input("enter mathematics's marks"))
dictionort.update({"phy " : y })

z = int(input("enter computer's marks"))
dictionort.update({"com " : z})
print(dictionort)

# Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)
values = { 9 ,  9.0}
print(values)#9

values = {9 , '9'}
print(values)

values = (float(9.0) , int(9))