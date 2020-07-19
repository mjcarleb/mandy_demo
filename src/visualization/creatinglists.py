list1 = [3, 5, 7, 8, 9, 5, 6, 7, 4, 3]
list2 = [1, 4, 5, 8, 3, 6, 9, 3, 5, 9]

final_list = [[(x+y) for y in list1 if y < 4] for x in list2 if x < 4]
print(final_list)