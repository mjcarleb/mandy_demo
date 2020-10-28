elements_list = None
elements_per_row = None
while True:
    try:
        elements_list = list(input("Please enter a list of elements to print a matrix from:"))

        elements_per_row = int(input("How many numbers would you like to have per row:"))
        break
    except ValueError:
        print("Please try again")
        continue
elements_list = [x.split() for x in elements_list.split(',')]
for i, item in enumerate(elements_list):
    if (i+1)%elements_per_row == 0:
        print(item)
    else:

        print(item, end=' ')
