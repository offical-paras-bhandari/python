# here file need to be closed
file = open("my_file.txt")
content = file.read()
print(content)
file.close()

# here file need to be closed
with open("my_file.txt") as file:
    content = file.read()
    print(content)

# Writing
with open("my_file.txt",mode="w") as file:
    file.write("i love you\n")

# appending
with open("my_file.txt",mode="a") as file:
    file.write("i love you")


