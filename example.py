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

while True:
    nightlife_vibe = input(
        "Nice, dinner is handled. What kind of nightlife vibe are you in the mood for after? "
        "(pick from dancing, drinks and vibes, singing, or laughing) "
    )

    try:
        nightlife_activity = demo.find_nightlife_activity(nightlife_vibe)
        break
    except ValueError as error:
        print(error)
        print("Please try again.")

print(
    f"You should check out {nightlife_activity['name']} for a "
    f"{nightlife_activity['activity_type']} tonight. "
)
print(f"Website: {nightlife_activity['website']} ")

more_nightlife = input(
    "If that pick is not quite your vibe, want to see a full list of similar spots? "
    "(yes/no/y/n) "
)
if more_nightlife.lower() == "yes" or more_nightlife.lower() == "y":
    nightlife_places = demo.list_nightlife_places(nightlife_vibe)
    print("Here are some more nightlife options for you: ")
    for place in nightlife_places:
        print(f"- {place['name']}: {place['website']}")
