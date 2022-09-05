class Snowflake:
    pass

flake = Snowflake()

print(dir(flake))


class Martian:
    """someone who lives on mars."""
    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln

    def __setattr__(self, name, value):
        print(f">>> You set {name} = {value}")
        self.__dict__[name] = value

    def __getattr__(self, name):
        print(f">>> Get the "{name}" attribute")
        

m = Martian("Klaus", "Iserlohn")

m1 = Martian("Rob", "Schenk")
m1.first_name = "Owen"
m1.last_name = "Phelps"
print(m1.__dict__)
print(m.__dict__)

m2 = Martian("Pierre", "Aberg")
print(f"First Name = {m2.first_name}")
print(f"Last Name = {m.last_name}")