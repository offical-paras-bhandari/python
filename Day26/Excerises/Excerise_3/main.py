with open("file1.txt") as file1:
    new_list1 = file1.readlines()
with open("file2.txt") as file2:
    new_list2 = file2.readlines()


int_new_list1 = [int(list) for list in new_list1]
int_new_list2 = [int(list) for list in new_list2]
result = [item for item in int_new_list1 if item in int_new_list1 and item in int_new_list2]
# Write your code above 👆

print(result)


