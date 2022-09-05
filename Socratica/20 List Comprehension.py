# List Comprehension || Python Tutorial || Learn Python Programming

squares =  []
for i in range(1,101):
    squares.append(i**2)

print(squares)


squares2 = [i**2 for i in range(1,101)]

print(squares2)

remainders5 = [x**2 % 5 for x in range(1,101)]
print(remainders5)

remainders11 = [x**2 % 11 for x in range(1, 101)]
print(remainders11)

movies = ["Star Wars", "Gandhi", "Casablanca", "Shawshank Redemption", "Toy Story", 
"Gone With The Wind", "Citizen Kane", "It's a Wonderful Life", "The Wizard of Oz",
"Gattaca", "Rear Window", "Ghostbusters", "To Kill A Mockingbird", "Good Will Hunting",
"2001: a Space Odyssey", "Raiders of the Lost Ark", "Groundhod Day", "Close Encounters of The Third Kind" ]

gmovies = []
for title in movies:
  if title.startswith("G"):
    gmovies.append(title)
print(gmovies)
# but this 4 line routine can be done in a single line with a list comprehension
gmovies = [title for title in movies if title.startswith("G")]
print(gmovies)
# we can the same answer with a single line of code.

# Lets complicate this example a bit more.
movies = [("Ctizen Kane", 1941),
          ("Spirited Away", 2001),
          ("It's a Wonderful World", 1946),
          ("Gattaca", 1997),
          ("No Country for Old Men", 2007),
          ("Rear Window", 1954),
          ("The Lord of the Rings: The Fellowship of the Ring", 2001),
          ("Groundhods Day", 1993),
          ("Close Encounters of the Third Kind", 1977),
          ("The Royal Tenenbaums", 2001),
          ("The Aviator", 2004),
          ("Raiders of the Lost Ark", 1981)  
           ]

# Task: Find all movies released before 2000.

pre2k = [title for (title, year) in movies if year < 2000]
print(pre2k)

# Scalar Multiplication
v = [2, -3, 1]
# Simple multiplication results in concatination not each element, the whole list
print(4*v)

print([2, 4, 6] + [1, 3])

w = [4*x for x in v]
print(w)

# The Cartesian Product

# If A and B are sets,
# then the Cartesian product
# is the set of pairs (a, b)
# where 'a' is in A and 'b' is in B.

# Example:
# A = {1, 3}
# B = {x, y}
# AxB = {(1, x), (1, y), (3, x), (3, y)}

A = [1, 3, 5, 7]
B = [2, 4, 6, 8]

cartesian product = [(a, b) for a in A for b in B]

print(cartesian_product)

