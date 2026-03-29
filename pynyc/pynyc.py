import random

ACTIVITIES = {
    "rainy": [
        "Go to The Met. Don't forget to check out Washington Crossing the Deleware!",
        "Catch a movie. If it's Tuesday, tickets are cheaper, so you can get a blue razz ICEE.",
        "Read performatively at the largest Barnes and Nobles in the world in Union Square.",
        "Check out the Natural History Museum. The planeterium is pretty cool.",
        "Go to a dog cafe and make a new bestfriend!",
    ],
    "sunny": [
        "Take a walk around Central Park. Bring a blanket to catch a tan on the Great Lawn",
        "Go to the Bronx zoo. Check out the crocodiles or feed the birds!",
        "Walk the High Line and enjoy the fresh air.",
        "Ride bikes on Governors Island. The ferry is free.",
        "Catch a game at Yankee Stadium or Citi Field. Choose wisely.",
        "Go shopping in Soho!"
    ],
    "freezing": [
        "Stay home. This is not negotiable.",
        "Go to Chelsea Market, and try everything.",
        "It is soup weather. Go get a bowl of pho.",
        "Go on a tour to find the best hot chocolate in the city.",
        "Grand Central. Just walk around and pretend you're in a movie.",
    ],
    "hot": [
        "Take the Staten Island Ferry to see the Statue of Liberty. It has AC.",
        "Head over to Rockaway Beach. It's only an hour from the city!!!.",
        "Go get ice cream and eat it before it melts!",
        "Find a shady spot in Central Park and don't move.",
    ],
    "perfect": [
        "Go outside immediately. These days are very rare.",
        "Just go for a walk. No destination necessary.",
        "Grab dinner with friends. Sit outside, enjoy the breeze, and people watch.",
        "Sit in Washington Square park and people watch.",
        "Bring a speaker and some friends to Central Park.",
        "Ride a bike along the Brooklyn Bridge and check out the skyline."
    ],  
}
ACTIVITIES["cold"] = ACTIVITIES["freezing"]
    
def find_restaurant(cuisuine:str, hours=12):
    restaurant_id = random.randint(0, 100)

def find_activity(weather: str) -> str:
    if weather.lower() not in ACTIVITIES:
        return f"'{weather}' is not valid. Try: rainy, sunny, freezing, cold, hot or perfect."
    return random.choice(ACTIVITIES[weather.lower()])