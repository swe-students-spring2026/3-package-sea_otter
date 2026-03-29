import pynyc as demo

print("Welcome to the our NYC weekend planner service. Having trouble to decide what to do? We got you!")

cuisine = input("Hi what you want for dinner? (American/Italian) ")
restaurant = demo.find_restaurant(cuisine)

print(f"Go to {restaurant}")