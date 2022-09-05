example = set()
print(dir(example))

'''
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', 
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', 
'__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', 
'__ixor__', '__le__', '__len__', 
'__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', 
'__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', 
'__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 
'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 
'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 
'symmetric_difference_update', 'union', 'update']
'''
print(help(example.add))
'''
Help on built-in function add:

add(...) method of builtins.set instance
    Add an element to a set.

    This has no effect if the element is already present.

None
'''
example_set = set()
example_set.add(42)
example_set.add(False)
example_set.add(3.14159)
example_set.add("Thorium")
print(example_set)
# For Sets the order does not matter.
# Sets do not contain duplicate elemtns.
# To see the length of a set use the length function len()
print(len(example_set))
# 4
# To remove an element from a set use the remove function
# help(example_set.remove)
'''
Help on built-in function remove:

remove(...) method of builtins.set instance
    Remove an element from a set; it must be a member.

    If the element is not a member, raise a KeyError.
'''
example_set.remove(42)
print(len(example_set))
print(example_set)

'''
Help on built-in function discard:

discard(...) method of builtins.set instance
    Remove an element from a set if it is a member.

    If the element is not a member, do nothing.
'''
# The remove method will return an error if you try to remove an element that does not exist.
# The discard method will not return an error if you delete an element that doesnt exist in the set.

# Intergers 1 -10
odds = set([1, 3, 5, 7, 9])
evens = set([2, 4, 6, 8, 10])
primes = set([2, 3, 5, 7])
composites = set([4, 6, 8, 9, 10])

odds.union(evens)

evens.union(odds)

print(odds)
print(evens)
print(odds.intersection(primes))
print(primes.intersection(evens))
print(primes.union(composites))
print(2 in primes)
print(6 in odds)
print(9 not in evens )
print(dir(primes))