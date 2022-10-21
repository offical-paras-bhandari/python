#scope#
# => avoid modifying global scope
enemies =1#global scope
def increase_enimies():
    global enemies # we can use global keyword to modify global variables that has same name.
    enemies+=2#local variable or local scope or local spaceg[imp]=> global and local having same name are diff variables
    print(f"enemies inside function {enemies}")
increase_enimies() 
print(f"enemies outside function {enemies}") 

# => instead we can use return statements 
# we can change the global variable by return statement
enemies =1#global scope
def increase_enimies_1():
    return enemies+1
enemies=increase_enimies_1() 
print(f"enemies outside function {enemies}") 