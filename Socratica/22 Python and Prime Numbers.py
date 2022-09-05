import math
import time
# Use python to write a series of functions to check if a number is prime.
# Recall the definition of prime number: A positive interger that is divisible by itself and one.

# Check all devisors from 2 through n-1.
# Skip 1 and n since every number is dividalbe by itself and 1.

def is_prime_v1(n):
    """Return true if 'n' is a prime number. False otherwise."""
    if n == 1:
        return False # 1 i not prime.
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

# test function
for n in range(1, 21):
    print(n,is_prime_v1(n))

# Time Function
t0 = time.time()
for n in  range(1, 10000):
    is_prime_v1(n)
t1 = time.time()
print("Time Required: ", t1 - t0)

# Next step, reduce the number of divisors we check.
# V2 test all divisors from 2 through sqrt(n)
def is_prime_V2(n):
    """ Return 'True' if 'n' is a prime number. False otherwise."""
    if n == 1:
        return False  # 1is not prime
    
    max_divisor = math.floor(math.sqrt(n))
    for d in range(2, 1 +  max_divisor):