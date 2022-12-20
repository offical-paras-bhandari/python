import random

names = ['BindaMomi', 'LaxmiMata', 'ParbatiMata', 'SaraswatiMata', 'RadhaMata']
# new_dict_names = {new_key:value for item in list}
students_score = {student: random.randint(1, 100) for student in names}
print(students_score)
# new_dict_names = {new_key:value for (key,value) in dictionary.items() if test}
students_passed = {student: score for (student, score) in students_score.items() if score >= 60}
print(students_passed)
