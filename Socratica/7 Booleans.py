# Booleans, Pythons only Logical Type. There is only two values, True and False. Both are Capitalized.

'''
>>> True
True
>>> true
Traceback (most recent call last):   
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> 
'''
# Booleans are commonly encoutered when comparing two objects.
# suppose a = 3
a = 3
b = 5
# to compare two numbers use the double equals operator.
a == b

'''
>>> a=3
>>> b=5
>>> a==b
False
'''
# The exclamation point is commonly used a logical NOT symbol in programming.
'''
>>> a != b
True
'''
# comparing two numbers, which is larger or smaller?
'''
a > b
False
a < b
True
'''

'''
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
'''

# All numbers except Zero are converted to True. 0 zero is always False.
'''
>>> bool(28)
True
>>> bool(-2.71828) 
True
>>> bool(0)
False
'''

# Strings can also be converted to Booleans, all strings except an empty string are True.
'''
>>> bool("Turning") 
True
>>> bool(" ")       
True
>>> bool("
'''