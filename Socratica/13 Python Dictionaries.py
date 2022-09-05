post = {"user_id":209, "message":"D5 E5 C5 C4 G4", "language":"English", "datetime":"20230215T124231Z", "location":(44.590533, -104.715556)}

print(post)
print(type(post))

post2 = dict(message="SS Cotopaxi", language="English")
print(post2)
# When you add new data using brakcets you have to put the item name in double perens.
post2["user_id"] = 209
post2["datetime"] = "19771116T093001Z"

print(post2)

# To see the message from the first post use the key name "message"
print(post['message'])
# Trying to access a value that does not exist will throw a key error.
# use the in operator to check of the key is in the dictionary.
if 'location' in post2:
    print(post2['location'])
else:
        print("The post does not contain a location value.")

# Another way is to try and retrieve the value but handle the possibility of an error.
# To do this, type the try command followed by a colon.
try:
    print(post['location'])
except KeyError:
    print("The post does not contain a location.")

# There is another way to to aceess a value in a dictionary and handle the possibility that it does not have a certian key.
# First, display the directroy for the post2  dictionary.
print(dir(post2))
# We will explaore the get method.
# To see what this does, use the help function
print(help(post2.get))

loc =  post2.get('location', None)
print(loc)

# A common task is to iterate over all the key/value pairs in a dictionary.
# A straight forward way to do is to loop over all the keys and get the value for each key.

for key in post.keys():
    value = post[key]
    print(key, "=", value)

for key, value in post.items():
    print(key, "=", value)
    