def Square_Numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_numbers = Square_Numbers([1,2,3,4,5])
# my nums  = [x*x for x in [1,2,3,4,5]]

print(my_numbers) # [1, 4, 9, 16, 25]

# for num in my_numbers:
    # Print nums

# currently our square numbers function is returning a list.
# how would we convert this to be a generator?
# All we have to do is replace the return keyword with yield.
# The Yield Keyword is what makes it a generator.

def  gen_square_numbers(nums):
    for i in nums:
        yield (i*i)

gen_my_nums = gen_square_numbers([1,2,3,4,5])
print(gen_my_nums)

# Now the function returns <generator object gen_square_numbers>
# Generators don't hold the entire answer like a typical return function would.
# It YIELDS one result at a time.
# It's waiting for us to ask for the next result.
#It hasn't actually computing anything yet.
# If we use the next() function it will print the answer.
print(next(gen_my_nums))

# At this point the generator is excusted and it will not yield more results.
# We can still use a for loop on a generator so you don't have to use the next() function
gen_my_nums = gen_square_numbers([1,2,3,4,5])
for nums in gen_my_nums:
    print(nums)

# You can convert a generator to a list to print out all the results at once.
print(list(gen_my_nums))