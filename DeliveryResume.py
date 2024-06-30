
Choice = input("select the food for Lunch or Breakfast or Dinner given below:")
food=input("which type of food wants South-Indian or North-Indian:")

#THIS IS FOR BREAKFAST
if(Choice == "Breakfast"):    
    if(food == "South-Indian"):
        Items =input("enter the food name to wants for breakfast :")
    
    if(Items == "iteli"):
            print("Thank You For Order You're Ordered",Items)
    elif(Items == "Dosa"):
        print("Thanks For Order This Is You're Ordered",Items)
 
#THIS IS FOR NORTH-INDIAN BREAKFAST

if(Choice == "Breakfast"):
    if(food == "North-Indian"):
        North_food =input("Enter you're food for breakfast:")
        if(North_food =="Lassi"):
            print("you are ordered",North_food)
        elif(North_food == "Maggie"):
            print("you are ordered",North_food)
    
    print("<<-----Thank You ----->>")
    
#THIS IS FOR SOUTH - INDIAN LUNCH

if(Choice == "Lunch"):
    if(food == "South-Indian"):
        South_lunch =input("name of food wants to eat")
        if(South_lunch == "Veg-Biriyani"):
            print("you are ordered",South_lunch)
        elif(South_lunch == "Paneer"):
            print("you are ordered",South_lunch)
        else:
            print("Not available",South_lunch)
        

   
if(Choice == "Lunch"):
     if(food == "North-Indian"):
         North_Lunch = input("Order food which type of North-Lunch:")
         if(North_Lunch == "Dal Tadaka"):
             print("you are ordered",North_Lunch)
         elif(North_Lunch == "Vada-Pav"):
             print("you are ordered",North_Lunch)
         else:
            print("Not Availbe",North_Lunch)
            
            
        
print("<<-----Thank You ----->>")


if(Choice == "Dinner"):
    if(food == "South-Indian"):
        South_Dinner=input("Enter The food which wants to eat in South Dinner:")
        if( South_Dinner == "curd rice"):
            print("you are ordered",South_Dinner)
        elif(South_Dinner =="Rajma Chaval"):
            print("you are ordered",South_Dinner)
        else:
            print("Not Availbe",South_Dinner)
            
            
            
if(Choice == "Dinner"):
    if(food =="North-Indian"):
        Dinner =input("enter the food:") 
        if(Dinner == "Samosa Pav"):
            print("Thank You For Order:",Dinner)
        elif(Dinner == "Non-veg Briyani"):
            print("Thank You For Order:",Dinner)
        else:
            print("Not Availbe",Dinner)
            
print("<<-----Thank You ----->>")





