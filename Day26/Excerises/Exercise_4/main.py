sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
new_list = sentence.split()
result = {word: len(word) for word in new_list}
print(result)

# print(new_list)
# result = {}
# for each in new_list:
#     result[each] = len(each)
# print(result)
