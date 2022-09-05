# Object Oriented Programming in Python

x = 1
print(type("Hello!"))
# <class 'str'>

print(type(x))
# <class 'int'>

# Defining a function
def Hello():
    print("Hello!")

print(type(Hello))

# Whenever you create something in Python you are creating an Object.
# An Object is an Instance of a Class.
# The Class defines the way in which that Object can interact with other things.

string = "hello"
print(string)
print(string.upper())

# the Dot(.) Operator acts on an object.
# In this case the method .upper acts on the object string.

# Create a Class called Dog
class Dog:
    def Bark(self):
        print("Bark!")

d = Dog()
d.Bark()
# Create a variable d and assign it to an instance of the class Dog.
# d is now an object that is of type Dog
print(type(d))
# <class '__main__.Dog'>
# %%
