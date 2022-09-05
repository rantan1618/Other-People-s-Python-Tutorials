# The functions in the random number module were NOT designed for cryptographry
import random
print(help(random.random))

# display 10 random numbers from interval [0, 1)]
# The random numbers represent a uniform distrabution
for i in range(10):
    print(random.random())

# what if you want to generate random numbers from a different interval?
# Generate random numbers from the internval [3-7]
# Call random()  in  [0,1)
# Scale number  (multiply by 4): in [0,4)
# Multiply by 4 because that's the width of the interval 3-7
# Add 3 to shift the number to the interval 3-7

def my_random():
    # Random, scale, shift, return...
    return 4*random.random() + 3

for i in range (10):
    print(my_random())

# random() and uniform() are both normal distrabutions.
# The mean is the average

# but there is an easier way to generate random numbers from any interval.
# Use the uniform function.

print(help(random.uniform))
# the random function can be used to built customized random number generators.

for i in range(10):
    print(random.uniform(3, 7))

# but there are other distrabutions where some groups of numbers are more likely to be chosen than others.
# the most widely encountered is the "Normal Distrabution" aka "The Bell Curve"
# A Normal Distrabution is completely described by just two numbers, The Mean and The Stand Deviation
# The mean is the average, it's where the Bell Curve Peaks.
# the Standard Deviation describes how wide or narrow the curve is
# To generate random numbers from a normal distrabution you use the normalvariate function
# When you call this function you must pass in both the mean and the standard deviation

# To generate 20 numbers from a bell curve with mean 0 and standard deviantion 1 you call the normalvariate function and pass in the two variables.

for i in range(20):
    print(random.normalvariate(0, 1))

# If you make the standard deviantion small the numbers will be tightly grouped.

for i in range(20):
    print(random.normalvariate(0, 0.2))

# If you change the mean to 5, you'll see that the random numbers are now bunched around 5.

for i in range(20):
    print(random.normalvariate(5, 0.2))

# sometimes you don't want a random number chosen from an infinite number of possibilities.
# for example, what if you want to simulate the roll of a 6 sided die?
# for this you use the randint function 
# randint(min, max)
# If you want a random interger between 1 and 6, call randint with the smallest possible interger and then the largest possible interger.
for i in range(20):
    print(random.randint(1, 6))

# There are even times when you want a random selection from a list of values which are not numbers.
# For example, suppose you want to write a program to play Rock, Paper, Scissors.
outcomes = ['Rock', 'Paper', 'Scissors']
# to pick a random value from this list use the choice function.
for i in range(20):
    print(random.choice(outcomes))

