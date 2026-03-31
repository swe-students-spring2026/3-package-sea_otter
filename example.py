import pynyc as demo

print("Welcome to the our NYC weekend planner service. Having trouble to decide what to do? We got you!")

cuisine = input("Hi what you want for dinner? (EXP: American/Italian/Chinese...etc.) ")
micheline = input("Do you prefer a Michelin restaurant?(yes/no/y/n)  ")
if(micheline.lower()=="yes" or micheline.lower()=="y"):
    micheline =True
else: 
    micheline=False
restaurant = demo.find_restaurant(cuisine,micheline)

print(f"Go to {restaurant}")


# Cafe
time = input("What time of day is it? (EXP: morning, afternoon, evening) ")
cafe = demo.get_cafe(time.lower())

print(f"You should check out {cafe}")
