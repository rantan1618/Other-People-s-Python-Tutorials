# Collect string / test length

input1 = input("Please enter a test string: ")

if len(input1) < 6:
    print("Your string is too short.")
    print("Please enter a string with at least 6 characters.")
 # Prompt user to enter number / test if even or odd.   
 
input2 = input("Please input an interger: ")
number = int(input2)
if number % 2 == 0:
    print("Your number is even.")
else:
    print("Your number is odd.")

# Scalene triangle: All sides have different lengths.
# Isosceles triangle: Two sides have the same length.
# Equailateral Triangle: All sides are equal.

a = int(input("The Legnth of side a = "))
b = int(input("The Legnth of side b = "))
c = int(input("The Legnth of side c = "))

if a != b and b != c and a != c:
    print("This is a scalene Triangle")
else a == b and b ==c:
    print("This is an equillateral triangle.")
else:
    print("This is an iscolces triangle.")

