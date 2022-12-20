import pandas

student_dict = {
    "names": ["paras", "shiva", "vishnu"],
    "age": [13, 34, 45]
}

student_data_df = pandas.DataFrame(student_dict)
print(student_data_df)

# loop through DataFrame
# looping through each of the column
# for (key, value) in student_data_df.items():
#     print(key)
#     print(value)

# loop through each of the row
for (index, row) in student_data_df.iterrows():
    print(row.names)


student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass
