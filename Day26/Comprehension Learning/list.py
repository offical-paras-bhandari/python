numbers = [1, 2, 3, 4, 5]
# new_list = [new_item for item in list if test] || [new_item for item in list]
new_number_list = [number + 1 for number in numbers]
print(new_number_list)

numbers = [1, 2, 3, 4, 5]
new_number_list = [number ** 2 for number in numbers if number > 2]
print(new_number_list)

names = ["BindaMomi", "LaxmiMata", "ParbatiMata", "SaraswatiMata", "RadhaMata"]
new_number_list = [name.upper() for name in names if len(name) > 8]
print(new_number_list)
