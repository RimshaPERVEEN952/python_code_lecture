def story():
# welcome message
    print("welcome")  
# instruction or requirements
    print("Fill in the blanks to create your story.\n") 
    name = input("enter your name : \t")
    place = input("enter your favourite place: \t")
    fruits_name = input("enter your favourite fruits : \t")
    mood = input("enter aout your mood")
    friend = input("enter your best friend name:\t")

    print("Now , here is your story")
    # lets create story
    my_story = (f"welcome! {name}, hope you are {mood} for your story\n"
                f"once upon a time, {name} went to {place}, before to visit {place} "
                f"{name} bring favourit friuts named {fruits_name} "
                f"with best friend {friend} , and really {mood}"
                f"that was the day that has begin a memorable day "
                )
    print(my_story)

# call function named story()
story()

# 2nd another
def data():
    # welcome msg
    print("wellcome!")
    #instruction
    print("Fill in the blanks to create your story.\n")
    fullName = input("enter your full name :\t")
    fatherName = input("enter your father name:\t")
    father_passion = input("enter your father passion:\t")
    mother_Name = input("enter your mother name:\t")
    mother_passion = input("enter your mother passion:\t")
    qualification = input("enter your qualification:\t")
    institute = input("enter your institute")
    goal = input("enter your goal: \t")

# lets make story
    my_story = (f"hellow! I am {fullName} . My father name is {fatherName}."
                f"he is a {father_passion}. My mother name is {mother_Name}. And she"
                f"is a {mother_passion}. I have completed {qualification}"
                f" from {institute} . My goal / aim is to be {goal} and I am doing"
                f"hard work to achive a bright future")
    print(my_story)

data()