# Numbers: int, float, complex
# Operations + - * / 

x = 28 # int
y = 28.0 # float

# Turn an int into a float
print(float(28))

# Floats turned into ints will be rounded first.
print(3.14) # float
int(3.14)
print(int(3.14))

# ints are narrower than floats
# floats are wider than ints

# Any float can be made into a complex number, but not vice versa.
x1 = 1.732
x2 = x1 + 0j
print(x2)
print(complex(x1))
 # floats are narrower than complex numbers
 # complex numbers are wider than floats

 # The four Arthematic Operations in Python

a = 2 #int
b = 6.0 # float
c = 12 + 0j #complex number

 # Addition
print(a + b)  # int  + float
# Subtraction
print(b - a)  # float  - int 
# Multiplication
print(a * 7)  # int  * int 
# Division
print(c / b)  # complex  / float 