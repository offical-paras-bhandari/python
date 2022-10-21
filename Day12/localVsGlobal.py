#scope#
enemies =1#global scope
def increase_enimies():
    enemies =2#local variable or local scope or local space
    print(f"enemies inside function {enemies}")
increase_enimies() 
print(f"enemies outside function{enemies}") 