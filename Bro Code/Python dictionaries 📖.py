# dictionary = A changable, unordered collection of unique key:value pairs
                # Fast because they use hashing, allow us to access a value quickly.


capitals = {
    "USA":"Washington DC",
    "India":"New Dehli",
    "China":"Beijing",
    "Russia":"Moscow"
}
capitals.pop("China")
# print(capitals["Germany"])  Returns an error.
# print(capitals.get["Germany"])

capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Las Vagas"})
print(capitals.keys())
print(capitals.values())
print(capitals.items())



for key,value in capitals.items():
    print(key,value)


# Use pop to remove items from a dictionary
# Clear will empty the dictionary 
capitals.clear()
print(capitals)