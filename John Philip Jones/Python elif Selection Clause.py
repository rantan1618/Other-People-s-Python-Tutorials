# Write a program that asks the user to enter their age.
# If they are 18 or older the program reports back and tells them to collect their polling card.
# if the user enters their age as 17 the program reports back their ages and informs them they can vote next year.
# however, if they are not old enough to vote and are not 17 the program again reports back their age and tells
# them they are too young to vote.
age = int(input("Please input your age: "))
if age >= 18:
    print("You are " + str(age) + " so collect your polling card.")
elif age == 17:
    print("You are " + str(age) + " so you can vote next year.")
else:
    print("You are " + str(age) + " so you are too young to vote.")
