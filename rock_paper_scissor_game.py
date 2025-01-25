import random

option = ["rock" , "paper" , "scissor"]
com_choice = random.choice(option)
# print(com_choice)

user_inp = input("please enter your choice\n 1. Rock \n 2. paper \n 3. scissor \t:..")

com_score= 0
round = 0
if(user_inp == com_choice):
        print(f"you select {user_inp} \n computer select {com_choice}")
        round= round
        com_score == com_score
        print(f"your score :{round}")
        print(f"computer score :{com_score}")
        print("Game has drawn")

elif((user_inp == "rock" and com_choice == option[2]) or(user_inp == "paper" and com_choice == option[1]) or(user_inp == "scissor" and com_choice == option[0])):
        round += 1
        print(f"your score :{round}")
        print("you Win game ")

else:
        round-= 1
        com_score +=1
        print(f"computer score :{com_score}")
        print("you lose")
        print(f"score :{round}")