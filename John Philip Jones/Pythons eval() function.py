number =input("Please enter a number: ")
double_number = number*2
print(double_number)

number =input("Please enter a number: ")
double_number = number*3
print(double_number)

print(len(number))
print(len(double_number))


calculation = input("Type a function for y = ")

for x in range(0,30,10):
    print("For x = ", x , " : Y = ", eval(calculation))
    