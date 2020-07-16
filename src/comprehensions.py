
print("==================================")
print(f"List Comprehensions:")
print("==================================")
print(f"List of numbers:  {[i for i in range(5)]}")
print(f"List of even numbers:  {[i for i in range(10) if i%2 == 0]}")

cols = [f"{letter}" for letter in "ABCDE"]
print(f"List of headings:  {cols}")
rows = [f"{j+1}" for j in range(5)]
print(f"List of rows:  {rows}")

cells = [f"({row}, {col})" for row in rows for col in cols]
print(f"List of (row, col) = {cells}")
print()

print("==================================")
print(f"Dictionary Comprehensions:")
print("==================================")
words = ["apple", "tomorrow", "earth"]
definitions = ["A red fruit subject to gravity", "The day after today", "A blue orb that revolves around the sun"]
my_dict = {words: definitions for words, definitions in zip(words, definitions)}
my_keys = my_dict.keys()
for k in my_keys:
    print(f"Definition of {k} is '{my_dict[k]}'")

##################################
# Sunday 7/19/20
# Flattening a list
##################################

# list of lists to flatten
nested_files = [["d0:f0", "d0:f1"],["d1:f0", "d1:f1", "d1:f2"]]

# NOTE:  l in nested_files before f in l (just as though it were outer loop first then inner loop)
flat_files = [list_item for inner_list in nested_files for list_item in inner_list]
print(f"Flattend files:  {flat_files}")

##############################
# Working with list of lists
##############################

# list of list of integers
l = [[1, 2, 3], [4, 5, 6], [7, 8]]

# convert to floats
fl = [[float(i) for i in fl] for fl in l]
print(f"floating list of lists:  {fl}")

##################################
# Sunday 7/19/20
# Creating a list of lists
##################################
l_of_l = [[i for i in range(3)] for j in range(5)]
print(f"List of lists:  {l_of_l}")
