# Let's now amend the program that implemented the specification from the last video in the playlist.
# Amendment: If the user enters their age as 17 they are STILL told that they are too young to vote 
# but in addition they are told can vote next year.
age = int(input("Please input your age: "))
if age >= 18:
    print("Collect your polling card.")
else:
    print("You are too young to vote.")
    if age == 17:
        print("You can vote next year.")