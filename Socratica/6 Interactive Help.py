# Interactive Help || Python Tutorial || Learn Python Programming
dir() # short for directory
# In Python 3.9.5 dir() produces this result:
# ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
# To view all builtin modules
print(dir(__builtins__))
# Print dir() Method list as a formatted List.
# lst = dir(__builtins__)
# print('dir(__builtins__):', *lst, sep='\n ')

'''
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 
'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 
'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 
'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 
'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 
'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 
'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 
'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 
'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 
'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 
'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 
'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 
'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', 
'__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', 
'__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 
'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 
'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 
'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 
'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 
'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 
'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 
'super', 'tuple', 'type', 'vars', 'zip']
'''



'''
>>> help(pow)
Help on built-in function pow in module builtins:
'''

'''
pow(base, exp, mod=None)
    Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments

    Some types, such as ints, are able to use a more efficient algorithm when
    invoked using the three argument form.
'''

print(pow(2, 10))
# Outputs 1024

# Altentive way to do powers.
print(2 **10)

# Learn about Hex
print(help(hex))
'''
Help on built-in function hex in module builtins:

hex(number, /)
    Return the hexadecimal representation of an integer.

    >>> hex(12648430)
    '0xc0ffee'

None
'''

# Learning about more Modules
print(help('modules'))