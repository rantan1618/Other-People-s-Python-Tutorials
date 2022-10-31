from faker import Faker
f = Faker()

for _ in range(10):
    print(f.unique.random_int(min=1,max=100))

for _ in range(5):
    print(f.bothify(letters="ABCDEFGH"))