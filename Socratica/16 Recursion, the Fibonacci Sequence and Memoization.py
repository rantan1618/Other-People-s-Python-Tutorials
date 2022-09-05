# Recursion, the Fibonacci Sequence and Memoization || Python Tutorial || Learn Python Programming
# Fibonacci Sequence
# Goal: Write Function to return nth item of Fibonacci Sequence.
# Fast, Clearly Written, Rock Solid

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 101):
    print(n, ":", fibonacci(n))

# Memoization
# Cache Values

fibonacci_cache = {}

def fibonacci(n):
    # If we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    # Compute the Nth term
    if n == 1: 
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    # Cache the value and return it 
    fibonacci_cache[n] = value
    return 
for n in range (1, 101):
    print(n, ":", fibonacci(n))

