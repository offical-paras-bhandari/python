# try:
#     # if fail
#     file = open("a_file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["sdfsdf"])
#
# except FileNotFoundError:
#     # run this
#     file = open('a_file.txt', "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"that key{error_message} does not exist")
#     # if success
# else:
#     content = file.read()
#     print(content)
#
# finally:
#     file.close()
#     print("file was closed")
#     raise TypeError("This is an error")


# **********************************************************************************************************************
# height = float(input("Height: "))
# weight = int(input("Weight: "))
#
# bmi = weight / height ** 2
#
# if height > 300:
#     raise ValueError("Human height should not over 3m")
# print(bmi)

# **********************************************************************************************************************

# # TODO: Catch the exception and make sure the code runs without crashing.
# fruits = ["Apple", "Pear", "Orange"]
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#
#         # Specific error
#     except IndexError:
#         print("fruit pie")
#         # if success no error occur
#     else:
#         print(fruit + " pie")
#
#
# make_pie(4)


# **********************************************************************************************************************

# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
#
# total_likes = 0
#
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         post['Likes'] = 0
#     else:
#         print(total_likes)
