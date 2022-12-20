with open("file1.txt") as file1:
    new_list1 = file1.readlines()
with open("file2.txt") as file2:
    new_list2 = file2.readlines()

result = [int(item) for item in new_list1 if item in new_list1 and new_list2]
# Write your code above 👆

print(result)


