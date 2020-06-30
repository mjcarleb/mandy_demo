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