names = ("Navin", "Kiran", "Harsh")
comps = ("Dell", "Apple", "MS")

zipped = zip(names,comps)
print(zipped)
zippe = list(zip(names,comps))
print(zipped)
zipped = set(zip(names,comps))
print(zipped)
zipped = dict(zip(names,comps))
print(zipped)

zipped = zip(names,comps)
for (a,b) in zipped:
    print(a,b)
