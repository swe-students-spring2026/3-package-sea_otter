import pynyc

print("Welcome to our NYC weekend planner service. Having trouble to decide what to do? We got you!")

cuisine = input("Hi which type of restaurant do you want for your awesome weekend? (EXP: American/Italian/Chinese...etc.) ")
micheline = input("Do you prefer a Michelin restaurant?(yes/no/y/n)  ")
if(micheline.lower()=="yes" or micheline.lower()=="y"):
    micheline =True
else: 
    micheline=False
restaurant = pynyc.find_restaurant(cuisine,micheline)

print(f"Go to {restaurant}")

#Activity
while True:
    weather = input("Let's find something to do. What's the weather like outside? "
    "(rainy, sunny, freezing, cold, hot, or perfect) ")
    activity = pynyc.find_activity(weather)
    if "not valid" in activity:
        print(activity)
    else:
        break

print(activity)

# Cafe
time = input("What time of day is it? (EXP: morning, afternoon, evening) ")
cafe = pynyc.get_cafe(time.lower())
print(f"You should check out {cafe}")

# Excursion
while True:
    excursion_category = input(
        "Looking for something for the daytime? What kind of excursion interests you? "
        "(nature, historic, or coastal) "
    )
    try:
        excursion = pynyc.find_excursion(excursion_category)
        break
    except ValueError as error:
        print(error)
        print("Please try again.")

print(
    f"You should check out {excursion['name']} in {excursion['location']}. "
)
print(f"Website: {excursion['website']} ")

more_excursions = input(
    "Want to see more options for this type of excursion? "
    "(yes/no/y/n) "
)
if more_excursions.lower() == "yes" or more_excursions.lower() == "y":
    excursion_list = pynyc.list_excursions(excursion_category)
    print("Here are some more excursion options for you: ")
    for place in excursion_list:
        print(f"- {place['name']}: {place['website']}")

while True:
    nightlife_vibe = input(
        "Nice, a cafe, acitivy, and dinner is handled. What kind of nightlife vibe are you in the mood for after? "
        "(pick from dancing, drinks and vibes, singing, or laughing) "
    )

    try:
        nightlife_activity = pynyc.find_nightlife_activity(nightlife_vibe)
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
    nightlife_places = pynyc.list_nightlife_places(nightlife_vibe)
    print("Here are some more nightlife options for you: ")
    for place in nightlife_places:
        print(f"- {place['name']}: {place['website']}")
