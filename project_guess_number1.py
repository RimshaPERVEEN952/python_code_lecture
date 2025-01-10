myNum = 35

while myNum:
    userNum = int(input("enter a num : 0-100(multiple of 5):\t"))
    if(userNum == myNum):
        print("congratulation you select accurate")
        break
    elif(userNum > myNum):
        print("your number is greater")

    else:
        print("your number is lessor")

print("____Now Game is Over____")