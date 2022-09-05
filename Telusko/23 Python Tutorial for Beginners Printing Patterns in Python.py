# Print a 4x4 hash grid.


#%%
print("# ")
print("# ")
print("# ")
print("# ")
# %%
print("# ", end="")
print("# ", end="")
print("# ", end="")
print("# ", end="")
# %%
for i in range(4):
    print("# ")
# %%
for i in range(4):
    for j in range(4):
        print("# ", end="")
    print()
# %%
for i in range(4):
    for j in range(i):
        print("# ", end="")
    print()
# %%
for i in range(4):
    for j in range(i+1):
        print("# ", end="")
    print()
# %%
for i in range(4):
    for j in range(4-i):
        print("# ", end="")
    print()
# %%
