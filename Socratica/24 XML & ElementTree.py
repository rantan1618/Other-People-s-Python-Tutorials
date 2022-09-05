import  xml.etree.ElementTree as ET
print(dir(ET))

# Pythons Inspect Module is built for inspecting python code.
from inspect import getmembers, isclass, isfunction
 # Display the classes in the ET module

 for (name, member) in getmembers(ET,isclass):
     if not name.startswith("_"):
         print(name)

# XML is a tree of Elements
