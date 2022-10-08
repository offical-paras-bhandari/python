
programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again.",
                          "Event":"An event is perform when whever user perform action"
                          }
#TODO - Defining dictionary


#TODO - Adding new item for dictionary
programming_dictionary["Loop"]="it is iteration of the program"

#TODO - printing Value of Key 
print(programming_dictionary["Bug"])

#TODO - Creating an empty dictionary
empty_list={}

#TODO - Wipe an existing
#programming_dictionary={}

#TODO - Edit an item in a dictionary
programming_dictionary["Bug"] = "A Bug is Error that makes program error"

print(programming_dictionary)

for Key in programming_dictionary:#TODO - Where Key is Bug and Value is Defination
    print(Key)
    print(programming_dictionary[Key])

