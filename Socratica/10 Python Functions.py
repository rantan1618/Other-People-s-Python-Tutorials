print(dir())
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']

def f():
    pass

# Calling a function after you have defined it.
f()
print(dir())
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'f']

def ping():
    return "Ping!"

print(ping())
# You can also store the return function as a variable:
x = ping()
print(x)
print(dir())

import math
print(dir(math))
'''
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', 
'__package__', '__spec__', 'f', 'ping', 'x'] 
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 
'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 
'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 
'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 
'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 
'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 
'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
'''
math_pi = 3.141592653589793
def volume(r):
    '''Returns the volume of a sphere with radius r.'''
    v = (4.0/3.0) * math_pi * r**3
    return v

print(volume(2))
# 33.510321638291124

def triangle_area(b, h):
    '''Return the area of a triangle with base b and height h.'''
    return 0.5 * b * h

print(triangle_area(3,6))

def cm(feet = 0, inches = 0):
    ''' Converts a length from feet and inches to centimeters.'''
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54
    return inches_to_cm + feet_to_cm

print(cm(feet = 5))
print(cm(inches = 70))
print(cm(feet = 5,inches = 8))
