age =  int(input("Please enter your age in years: "))
income = int(input("Please enter your annual income: "))

if (age >= 18) and (income >= 15000):
    print("You can apply for a loan.")
else:
    print("You CANNOT apply for a loan.")
    