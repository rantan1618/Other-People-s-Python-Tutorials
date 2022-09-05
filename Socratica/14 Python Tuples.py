import sys, timeit

# List Example
prime_numbers = [2, 3, 5, 7, 11, 13, 17]

# Tuple Example
perfect_numbers = (1, 4, 9, 16, 25, 36)

# Display Lengths
print("# Primes = ", len(prime_numbers))
print("# Squares = ", len(perfect_numbers))

# Iterate over both sequances
for p in prime_numbers:
    print("Primes: ", p)
for p in perfect_numbers:
    print("Squares: ", p)

print("List Methods")
print(dir(prime_numbers))
# List Methods
'''
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__',
 '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
  '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__',
   '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
    '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
     '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index',
      'insert', 'pop', 'remove', 'reverse', 'sort']
'''
print(80*"-")
print("Tuple Methods")
print(dir(perfect_numbers))
'''
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__',
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__',
  '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
   '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__',
    '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
'''

print("Sys Methods")
print(dir(sys))
'''
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__',
 '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__',
  '__unraisablehook__', '_base_executable', '_clear_type_cache', '_current_frames', '_debugmallocstats',
   '_enablelegacywindowsfsencoding', '_framework', '_getframe', '_git', '_home', '_xoptions',
    'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook',
     'builtin_module_names', 'byteorder', 'call_tracing', 'copyright', 'displayhook', 'dllhandle',
      'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags',
       'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth',
        'getallocatedblocks', 'getdefaultencoding', 'getfilesystemencodeerrors', 'getfilesystemencoding',
         'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval',
          'gettrace', 'getwindowsversion', 'hash_info', 'hexversion', 'implementation', 'int_info',
           'intern', 'is_finalizing', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path',
            'path_hooks', 'path_importer_cache', 'platform', 'platlibdir', 'prefix', 'pycache_prefix',
             'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setprofile',
              'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout',
               'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions', 'winver']
'''
print(help(sys.getsizeof))

list_eg = [1, 2, 3, "a", "b", "c", True, 3.141159]
tuple_eg = (1, 2, 3, "a", "b", "c", True, 3.141159)

print("List size = ", sys.getsizeof(list_eg))
print("Tuple size = ", sys.getsizeof(tuple_eg))

# Lists
# Add Data, Remove Data, Change Data

# Tuples
# Cannot be changed, Immutable, Made quickly

list_test = timeit.timeit(stmt="[1,2,3,4,5]", number=1000000)

tuple_test = timeit.timeit(stmt="(1,2,3,4,5)", number=1000000)

print("List Time: ", list_test)
print("Tuple Time: ", tuple_test)

empty_tuple = ()
test1 = ("a")
test2 = ("a", "b")
test3 = ("a", "b", "c")

print(empty_tuple)
print(test1)
print(test2)
print(test3)

# Alternitive Construction of Tuples

test_1 = 1,
test_2 = 1, 2
test_3 = 1,2,3

print(test_1)
print(test_2)
print(test_3)

print(type(test_1))
print(type(test_2))
print(type(test_3))

# Tuple with 1 element

# (age, country, knows_python)
survey = (27, "Vietnam", True)

age = survey[0]
country = survey[1]
knows_python = survey[2]

print("Age = ", age)
print("Country = ", country)
print("Knows Python = ", knows_python)

country = ("Australia",)
print(country)