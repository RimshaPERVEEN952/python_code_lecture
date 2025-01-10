import  random
target = random.randint(1 , 10)
while True:
    user = int(input("enter num 1 - 10: \t"))
    if(user == target):
        print("you have successfully completed")
        break
    elif(user > target):
        print("your number is too greater")
    else:
        print("your number is to lessor")
print("----Game is OVER-----")