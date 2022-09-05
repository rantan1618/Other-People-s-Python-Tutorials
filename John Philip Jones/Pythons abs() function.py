tempeture = eval(input("Please enter the tempeture: "))

if tempeture > 0:
    print("The tempeture is", tempeture, "degress centigrade", setp=" ")
elif tempeture == 0:
    print("The Tempeture is 0 degress centigrade.")
else:
    print("The Tempeture is" abs(tempeture), "degress centrigrade below zero". sep=" ")


complex_number = 3 + 4j
magnaitude = abs(complex_number)
print("The magnaitude of the complex number is", magnaitude, sep=" ")


a = abs(-5)
b = abs(5)
c = abs(+5)
print(a, b, c)

x = abs(-5.0)
y = abs(5.0)
z = abs(+5.0)
print(x,y,z)

magnaitude = abs(3+4j)
print(magnaitude)