#Funciton With Outputs

def format_name(fname,lname):
    if fname =="" and lname == "":
        return "you didn't provide valid name"
    formated_f_name =  fname.title()#TODO -  title() is returning and formated_f_name is holding the value
    formated_l_name = lname.title()
    return f"My First Name is {formated_f_name} and Last Name is {formated_l_name}"

print(format_name("paras","bhandari"))
formated_string = format_name("paras","bhandari")
print(formated_string)
#TODO - Return at early stage
formated_string = format_name(input("What is your first name"),input("What is your last name"))
print(formated_string)

#TODO - Docstring 
string=""" Here the data can be
writen in multiple line"""
#TODO - unlike string = "string
#TODO - " => it is invalid to give new line because interpeter does not understand
#TODO - it is also know as multiline commet
print (string)