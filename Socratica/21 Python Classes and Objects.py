class User:
    pass

user1 = User()

# user1 is an "instance" of User()
# user1 is an "object"
# To attatch data to the object you first type the name of the object and dot and the name of the variable and then give it a value.

user1.first_name = "Dave"
user1.last_name = "Bowman"

# We call them "fields", they store data specific to user1

print(user1.first_name)
print(user1.last_name)

# Let's create stand alone variables that are not attached to an object
first_name = "Arthur"
last_name = "Clarke"
print(first_name, last_name)
print(user1.first_name, user1.last_name)

user2 = User()
user2.first_name = "Frank"
user2.last_name = "Poole"

# Class Features
# Methods
# Intitialization
# Help Text
# We can turn our simple class into a data powerhouse.
# The first feature we will add is an init method. A Function inside a class is called a method.
# init method
# init = initialization
# Some languages call a method a aka = "Constructor"

import datetime

class User3:
    """A member of FriendFace. For now we are only their name and birthday.
    But soon we will store an uncomfortable amount of user information.
    """
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday # yyyymmdd
        
        # extract the first and last name
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[1]
    #  Let's add another method to user class that will return the age of the user in years.
    def age(self):
        """ Return the age of the user."""
    # First, get today's date:
        today = datetime.date(2001, 5, 12)
    # Next, convert the birthday string into a date object.
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
    # With these three intergers we can create a date object for the users birthday.
        dob = datetime.date(yyyy, mm, dd) # date of birth.
    # If you compute the difference between today and the birthday you get a time delta object.
    # The time delta object has a field called days.
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)
    # Ignoring leap years we can now compute the age in years be dividing by 365

user = User3("Dave Bowman", "19710315")
print(user.name)
print(user.birthday)
print(user.first_name)
print(user.last_name)

print(user.age())
# the self keyword is only used when writing the method.
 print(help(user))
