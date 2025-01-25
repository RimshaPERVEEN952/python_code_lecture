import random
import string

val = random.choice(['2' , "3" , "4" , "D" ,"f"])
print(val)

print(string.ascii_letters)
print(string.digits)
print(string.hexdigits)
print(string.punctuation)
pass_lan = 10
password = ""
char = string.ascii_letters + string.digits +string.hexdigits + string.punctuation
for i in range(pass_lan):
    password += random.choice(char)

print("Your Passwaord has been generated",password)