welcome = "Hello World"
print(welcome)
for character in welcome:
    print(character)
    ansi_value = ord(character)
    print("The ANSI value for", character, "is", ansi_value, sep=" ")