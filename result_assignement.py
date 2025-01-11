print("firstly enter your marks of given subject to show your result")
eng_marks = int(input("\t enter your marks(english):\t"))
urdu_marks = int(input("\t enter your marks(Urdu):\t"))
pst_marks = int(input("\t enter your marks(PST):\t"))
math_marks = int(input("\t enter your marks(Math):\t"))
phy_marks = int(input("\t enter your marks(Physics):\t"))
comp_marks = int(input("\t enter your marks(Computer):\t"))
percentage =((eng_marks + phy_marks+urdu_marks + pst_marks+math_marks+comp_marks) /550)* 100
if(percentage >= 80):
    print(f"your percentage is {percentage}"
          f" Congrtulation for your Grade :\t A+")
elif(percentage >= 70):
    print(f"your percentage is {percentage}"
          f" Congrtulation for your Grade :\t A")
elif(percentage >= 60):
    print(f"your percentage is {percentage}"
          f" Congrtulation for your Grade :\t B")
elif(percentage >= 50):
    print(f"your percentage is {percentage}"
          f" Congrtulation for your Grade :\t C")
elif(percentage >= 40):
    print(f"your percentage is {percentage}"
          f"your Grade :\t D")
else:
    print(f"your percentage is {percentage}"
          f"and you failed in exams")