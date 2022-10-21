game_level=1
enemies_1 =["skeleton","demons","dragons"]
if game_level < 3:
    enemies_appears_1 = enemies_1[0]

print(enemies_appears_1)#this block_scope [enemies_appear] is variable created inside block of code 
                    #where it is used it can be call from outside of the block(function)
                    
                    
                    
"""If it is define inside function than it is not accessible from outside of the  fucntion"""
game_level=0
enemies_2 =["skeleton","demons","dragons"]
def enemies():
    if game_level < 3:
        enemies_appear = enemies_2[0]
        print(enemies_appear)
enemies()
    

