##########Not Finished but helpful,it's process are helpfull for further projects########
from art import logo,vs
from game_data import data
import random

new_data_list= {}
new_second_data_list= {}

Values=[]
Values_1=[]
data_length =1

def extracting_information_from_A():
    random_data_a=random.choice(data)
    
    for list_data in random_data_a:
        #Adding new data in from of Key and Value in new list
        new_data_list[list_data]= random_data_a[list_data]  
        Values.insert(len(new_data_list)-1,new_data_list[list_data])
        """new_data_list which is type  of dictionary carry Data(Values) with repective Keys"""  
    return (f"Compare A:{Values[0]}, a {Values[2]}, from {Values[3]}" )  

def extracting_information_from_B():
    
    random_data_b=random.choice(data)
    
    for list_data in random_data_b:
        #Adding new data in from of Key and Value in new list
        new_second_data_list[list_data]= random_data_b[list_data]  
        Values_1.insert(len(new_second_data_list)-1,new_second_data_list[list_data])
        """new_data_list which is type  of dictionary carry Data(Values) with repective Keys"""  

    return (f"Compare B:{Values_1[0]}, a {Values_1[2]}, from {Values_1[3]}" )    

def start():
    print(logo)
   
    # compare_B = extracting_information_from_B()
    compare_A = extracting_information_from_A()           
    print(compare_A) 
    finised = False
    temp=""
    while not finised: 
        print(Values)      
        print(temp)
        print(vs)
        compare_B = extracting_information_from_B() 
        print(Values_1)
        print(compare_B)
        
        userchoices = (input("Who has more followers? Type: 'A' or 'B': "))
        if(userchoices=='A'):
            A=str(Values[1])
            B=str(Values_1[1])

            if(int(A)>int(B)):
                print("you are correct.")
                temp=compare_A                
            else:                    
                print("you arenot correct.")
                return                         
    
        else:
            A=str(Values[1])
            B=str(Values_1[1])
            if(int(B)>int(A)):
                print("you are correct.")
                temp=compare_B
            else:
                print("you arenot correct.")
                return                   
            
           
start()

###############################################################################--Rough stuff--############################################################################



# key =['name', 'country'] -etc
# def extracting_information_from_B():
#     random_data=random.choice(data)
#     for list_data in random_data:
#     new_second_data_list[list_data] = random_data[list_data]    
#     #Compareing With key and NewDatalist
#     for key in keys_Comparing:
#        if key in new_second_data_list:
#            Values_1.append(new_second_data_list[key])

#     """new_data_list whith is type list carry Data(Values) with repective Keys"""      
#     print(f"Compare B:{Values_1[0]}, a {Values_1[1]}, from {Values_1[1]}" ) 
     



# Values=[]
# Values_1=[]
# data = [
#     {
#         'name': 'Instagram',
#         'follower_count': 346,
#         'description': 'Social media platform',
#         'country': 'United States'
#     },
#     {
#         'name': 'Cristiano Ronaldo',
#         'follower_count': 215,
#         'description': 'Footballer',
#         'country': 'Portugal'
#     },
#     {
#         'name': 'Ariana Grande',
#         'follower_count': 183,
#         'description': 'Musician and actress',
#         'country': 'United States'
#     },
#     {
#         'name': 'Dwayne Johnson',
#         'follower_count': 181,
#         'description': 'Actor and professional wrestler',
#         'country': 'United States'
#     },
# ]
# hello={"sdfdsf",":","sdf"}
# print(len(hello))
# def extracting_information_from_A():
#     random_data = random.sample(data,1)
#     print(random_data)
#     list_data=""
#     for list_data in random_data:
#     #     #Adding new data in from of Key and Value in new list
#     #     new_data_list= random_data[list_data]  
#     #     print (new_data_list)    
#     #     Values.insert(len(new_data_list)-1,new_data_list[list_data])
#     #     """new_data_list whith is type list carry Data(Values) with repective Keys"""  
#     # print (Values)    
#         print(random_dataa)
#         #Values.insert(len(new_data_list)-1,new_data_list)
#         #print(Values)
#     # print (f"Compare A:{Values[0]}, a {Values[2]}, from {Values[3]}" )   
  
# def extracting_information_from_A():
#     random_data=random.sample(data,data_length)
#     print(random_data)
#     for list_data in random_data:
#         #Adding new data in from of Key and Value in new list        
#         new_data_list[list_data] = random_data[list_data]  
#         Values.append(new_data_list[list_data])
#         print(new_data_list[list_data])
# #         Values_1.append(new_data_list[list_data])
#         """new_data_list whith is type list carry Data(Values) with repective Keys"""           
#     return print(f"Compare A:{Values[0]}, a {Values[2]}, from {Values[3]}" )    

# extracting_information_from_A = extracting_information_from_A()
# print (extracting_information_from_A)



# from typing import Counter


# travel_log = [
#    {"coutnry": "France",
#     "cities_visited":["Paris","Lile","Dijon"],
#     "toal_visited":12 },
   
#    {
#     "country":"Nepal",
#     "cities_visited":["Birtamode","Kathmandu"], 
#     "toal_visited":2
#     }
# ]
# print(travel_log[0]["coutnry"])

