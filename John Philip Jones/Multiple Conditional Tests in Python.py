# Specification
# Write a program that asks users to enter a percentage mark for a module of study.
# the program prints the module grade as either distinction, merit, pass or fail
# depending on the percentage of mark earned.

# A mark of 70% and above is awarded a distinction.
# A mark in the range of 60% through 69% is awarded a merit.
# A mark in the range of 40% through 59% is awarded a pass.
# Marks less than 40% are awarded a fail.

module_mark = ""
percentage_mark = int(input("Enter the percentage mark: "))

if percentage_mark >= 70:
    module_mark = "Distinction"
elif percentage_mark >= 60:
    module_mark = "Merit"
elif percentage_mark >= 40:
    module_mark = "Pass"
else:
    module_mark = "Fail"

print("For the percentage mark of " + str(percentage_mark) + " the grade awarded is a " + str(module_mark))