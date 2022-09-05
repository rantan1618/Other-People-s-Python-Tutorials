# First class functions allow us to treat functions like any other object.
# We can pass functions as arguments to another function.
# We can return functions.
# and we can assign functions to variables.
# Closures all us to take advancte of first-class functions.
# and return an inner fuction that remembers and has access to 
# variables local to the scope in which they were created.

# we have an outer_function that doesn't take any parameters.
# def outer_function():
    # Within the outer_function there's a local variable called  message
    message = "Hi"
    # then, create an inner_function
#    def inner_function:
#       print(message)
#    return inner_function()

# outer_function()

# Decorate is a function that takes another function as an argument
# adds some kind of functionality, and then returns another function.
# all of this without altering the orignal source code of the function you passed in.

def decorator_function(original_function):
    def wrapper_function():
        print(original_function)
    return wrapper_function

def display():
    print("display function ran)

decoracted_display = decorator_function(display)

decorated_display()
