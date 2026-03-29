import random
from typing import Final, TypedDict

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



restaurant_list ={"American":{1:"Carmine's", 2:"Jacob's Pickles", 3:"Nightly"}, 
                  "Italian":{1:"", 2:""},
                  "Chinese":{1:""}
    
}
    
def find_restaurant(cuisuine:str, hours:int| None =12):
    restaurant_id = random.randint(0, 100)
    return "Clock tower wellington"

def find_activity(weather: str) -> str:
    if weather.lower() not in ACTIVITIES:
        return f"'{weather}' is not valid. Try: rainy, sunny, freezing, cold, hot or perfect."
    return random.choice(ACTIVITIES[weather.lower()])

class Venue(TypedDict):
    name: str
    website: str

class NightlifeCategory(TypedDict):
    activity_type: str
    places: list[Venue]

class NightlifeRecommendation(Venue):
    vibe: str
    activity_type: str

NIGHTLIFE_OPTIONS: Final[dict[str, NightlifeCategory]] = {
    "dancing": {
        "activity_type": "nightclub",
        "places": [
            {"name": "House of Yes", "website": "https://www.houseofyes.org/"},
            {"name": "Marquee New York", "website": "https://marqueeny.com/"},
            {"name": "Nebula", "website": "https://www.nebulanewyork.com/"},
            {"name": "Elsewhere", "website": "https://www.elsewherebrooklyn.com/"},
        ],
    },
    "music and vibes": {
        "activity_type": "bar",
        "places": [
            {"name": "The Django", "website": "https://www.thedjangonyc.com/"},
            {"name": "Skinny Dennis", "website": "https://skinnydennisbrooklyn.com/"},
            {"name": "Bar Lunatico", "website": "http://www.barlunatico.com/"},
            {"name": "Nublu 151", "website": "https://nublu.net/nublu-151/"},
        ],
    },
    "singing": {
        "activity_type": "karaoke",
        "places": [
            {"name": "Planet Rose", "website": "https://planetrose.com/"},
            {"name": "Sing Sing Avenue A", "website": "https://www.singsingavea.com/"},
            {"name": "Space Karaoke Bar & Lounge", "website": "https://spacekaraokebar.com/"},
            {"name": "Karaoke City", "website": "https://www.karaokecityny.com/"},
        ],
    },
    "laughing": {
        "activity_type": "comedy club",
        "places": [
            {"name": "Comedy Cellar", "website": "https://www.comedycellar.com/"},
            {"name": "Gotham Comedy Club", "website": "https://www.gothamcomedyclub.com/"},
            {"name": "New York Comedy Club", "website": "https://newyorkcomedyclub.com/"},
            {"name": "The Stand", "website": "https://www.thestandnyc.com/"},
        ],
    },
}

VIBE_ALIASES: Final[dict[str, str]] = {
    "bar": "music and vibes",
    "club": "dancing",
    "clubbing": "dancing",
    "comedy": "laughing",
    "dance": "dancing",
    "dancing": "dancing",
    "karaoke": "singing",
    "laughing": "laughing",
    "music": "music and vibes",
    "music and vibes": "music and vibes",
    "nightclub": "dancing",
    "singing": "singing",
    "vibes": "music and vibes",
}

def _normalize_vibe(vibe: str) -> str:
    normalized_vibe = vibe.strip().lower().replace("-", " ").replace("_", " ")
    normalized_vibe = " ".join(normalized_vibe.split())

    if normalized_vibe not in VIBE_ALIASES:
        valid_vibes = ", ".join(sorted(NIGHTLIFE_OPTIONS))
        raise ValueError(
            f"Unsupported vibe '{vibe}'. Choose from: {valid_vibes}."
        )

    return VIBE_ALIASES[normalized_vibe]

def list_nightlife_places(vibe: str) -> list[Venue]:
    """Return NYC nightlife options for a given vibe."""
    normalized_vibe = _normalize_vibe(vibe)
    places = NIGHTLIFE_OPTIONS[normalized_vibe]["places"]
    return [place.copy() for place in places]

def find_nightlife_activity(vibe: str) -> NightlifeRecommendation:
    """Select and return one random NYC nightlife activity (as dict) that matches the vibe."""
    normalized_vibe = _normalize_vibe(vibe)
    activity = NIGHTLIFE_OPTIONS[normalized_vibe]
    venue = random.choice(activity["places"])

    return {
        "vibe": normalized_vibe,
        "activity_type": activity["activity_type"],
        "name": venue["name"],
        "website": venue["website"],
    }
