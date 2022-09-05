# Specification:
# A bank will offer a customer a loan if they are 18 or over and have an annula income
# of at least $15000. Write a program that will , based on a customers age and income,
# produce a decision on whether they will be offered a loan.

age =  int(input("Please enter your age in years: "))
income = int(input("Please enter your annual income: "))

if (age >= 18) and (income >= 15000):
    print("You can apply for a loan.")
else:
    print("You CANNOT apply for a loan.")
    