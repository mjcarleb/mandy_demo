list = [[2,3,4], [5,8,9]]
flattened_list = [item for sublist in list for item in sublist]
print(flattened_list)

#Equivalent to starting at the farthest to the left for loop and work way in
l = [[1,2,3],[5,6,8], ['python','is','hard']]
flat_list = []
for sublist in l:
    for item in sublist:
        flat_list.append(item)
print(flat_list)