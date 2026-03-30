import json
import random
from pathlib import Path
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

def _load_restaurants() -> dict[str, dict[int, str]]:
    data_path = Path(__file__).resolve().parent / "data" / "restaurant_list.json"
    with data_path.open("r", encoding="utf-8") as data_file:
        payload = json.load(data_file)

    return {
        cuisine: {int(index): name for index, name in places.items()}
        for cuisine, places in payload.items()
    }

restaurant_list: Final[dict[str, dict[int, str]]] = _load_restaurants()

def _load_michelin() -> dict[str, dict[int, str]]:
    data_path = Path(__file__).resolve().parent / "data" / "michelin_nyc.json"
    with data_path.open("r", encoding="utf-8") as data_file:
        payload = json.load(data_file)

    grouped: dict[str, list[str]] = {}
    for restaurant in payload.get("restaurants", []):
        cuisine = str(restaurant.get("cuisine", "")).strip()
        name = str(restaurant.get("name", "")).strip()
        if not cuisine or not name:
            continue
        if cuisine not in grouped:
            grouped[cuisine] = []
        if name not in grouped[cuisine]:
            grouped[cuisine].append(name)

    return {
        cuisine: {index + 1: name for index, name in enumerate(names)}
        for cuisine, names in grouped.items()
    }


michelin_restaurants_list: Final[dict[str, dict[int, str]]] = _load_michelin()
    
def find_restaurant(cuisuine: str, michelin:bool| None = False,hours: int | None = 12):
    
    c_list = ["american","italian","chinese","french","japanese","mexican","indian","korean","thai"]
    for c in c_list:
        if cuisuine.lower()[0:2]==c[0:3]:
            cuisuine = c
            break
    if cuisuine not in c_list:
        return "Google and ask it to generate one restaurant for this cuisine, we don't have a great choice of this yet oops."
    
    restaurant_id = random.randint(0, len(restaurant_list[cuisuine])) #randomize one restaurant_id for a specific cuisuine
    restaurant = restaurant_list[cuisuine][restaurant_id] #here's the generated restaurant
    return restaurant

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
            {"name": "Marquee New York", "website": "https://taogroup.com/venues/marquee-new-york/"},
            {"name": "Nebula", "website": "https://nebulanewyork.com/"},
            {"name": "Elsewhere", "website": "https://www.elsewhere.club/"},
            {"name": "Avant Gardner", "website": "https://www.avant-gardner.com/"},
            {"name": "Brooklyn Mirage", "website": "https://www.avant-gardner.com/"},
            {"name": "Le Bain", "website": "https://www.lebainnewyork.com/"},
            {"name": "Public Records", "website": "https://publicrecords.nyc/"},
            {"name": "Good Room", "website": "https://www.goodroombk.com/"},
            {"name": "Harbor NYC", "website": "https://www.harbornewyorkcity.com/"},
            {"name": "Somewhere Nowhere NYC", "website": "https://www.somewherenowherenyc.com/"},
            {"name": "Superior Ingredients", "website": "https://www.si-bk.com/"},
            {"name": "Musica", "website": "https://musicanewyork.net/"},
            {"name": "SILO Brooklyn", "website": "https://www.silobrooklyn.com/"},
        ],
    },
    "music and vibes": {
        "activity_type": "bar",
        "places": [
            {"name": "The Django", "website": "https://www.thedjangonyc.com/"},
            {"name": "Skinny Dennis", "website": "https://skinnydennisbrooklyn.com/"},
            {"name": "Bar Lunatico", "website": "https://www.barlunatico.com/"},
            {"name": "Nublu 151", "website": "https://nublu.net/"},
            {"name": "Employees Only", "website": "https://www.employeesonlynyc.com/"},
            {"name": "Attaboy", "website": "https://attaboy.us/"},
            {"name": "The Dead Rabbit", "website": "https://www.thedeadrabbit.com/"},
            {"name": "Please Don't Tell (PDT)", "website": "https://www.pdtnyc.com/"},
            {"name": "The Back Room", "website": "https://www.backroomnyc.com/"},
            {"name": "Kind Regards", "website": "https://kindregardsnyc.com/"},
            {"name": "Mister Paradise", "website": "https://www.misterparadisenyc.com/"},
            {"name": "The Rum House", "website": "https://www.therumhousenyc.com/"},
            {"name": "Bathtub Gin", "website": "https://www.bathtubginnyc.com/"},
            {"name": "The Crown", "website": "https://www.thecrownnyc.com/"},
        ],
    },
    "singing": {
        "activity_type": "karaoke",
        "places": [
            {"name": "Planet Rose", "website": "https://www.planetrosenyc.com/"},
            {"name": "Sing Sing Avenue A", "website": "https://www.singsingavea.com/"},
            {"name": "Space Karaoke Bar & Lounge", "website": "https://spacekaraoke.com/"},
            {"name": "Karaoke City", "website": "https://karaokecitynyc.com/"},
            {"name": "Karaoke Boho", "website": "https://www.karaokeboho.com/"},
            {"name": "Gagopa Karaoke", "website": "https://www.gagopakaraoke.com/"},
            {"name": "Den Social Karaoke", "website": "https://www.densocial.com/karaoke"},
            {"name": "Karaoke K", "website": "https://karaokek.com/"},
            {"name": "Duet 35 Karaoke", "website": "https://www.karaokeduet.com/"},
            {"name": "Duet 48 Karaoke", "website": "https://www.karaokeduet.com/"},
            {"name": "Insa", "website": "https://insabrooklyn.com/"},
            {"name": "Baby Grand", "website": "https://www.babygrandnyc.com/"},
            {"name": "RPM Underground", "website": "https://rpmunderground.us/"},
            {"name": "Sing Sing Karaoke St. Marks", "website": "https://www.karaokesingsing.com/"},
        ],
    },
    "laughing": {
        "activity_type": "comedy club",
        "places": [
            {"name": "Comedy Cellar", "website": "https://www.comedycellar.com/"},
            {"name": "Gotham Comedy Club", "website": "https://www.gothamcomedyclub.com/"},
            {"name": "New York Comedy Club", "website": "https://newyorkcomedyclub.com/"},
            {"name": "The Stand", "website": "https://thestandnyc.com/"},
            {"name": "Stand Up NY", "website": "https://standupny.com/"},
            {"name": "Dangerfield's", "website": "https://www.dangerfields.com/"},
            {"name": "The Grisly Pear Comedy Club", "website": "https://www.grislypearstandup.com/"},
            {"name": "EastVille Comedy Club", "website": "https://www.eastvillecomedy.com/"},
            {"name": "Broadway Comedy Club", "website": "https://www.broadwaycomedyclub.com/"},
            {"name": "LOL Times Square Comedy Club", "website": "https://www.loltimesquare.com/"},
            {"name": "The Tiny Cupboard", "website": "https://www.thetinycupboard.com/"},
            {"name": "Q.E.D. Astoria", "website": "https://qedastoria.com/"},
            {"name": "The Creek and the Cave", "website": "https://www.thecreekthecave.com/"},
            {"name": "West Side Comedy Club", "website": "https://www.westsidecomedyclub.com/"},
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

class Excursion(TypedDict):
    name: str
    location: str
    website: str

class ExcursionCategory(TypedDict):
    excursion_type: str
    places: list[Excursion]

EXCURSION_OPTIONS: Final[dict[str, ExcursionCategory]] = {
    "nature": {
        "excursion_type": "nature",
        "places": [
            {
                "name": "Bear Mountain State Park",
                "location": "Bear Mountain, NY",
                "website": "https://parks.ny.gov/parks/13/details.aspx",
            },
            {
                "name": "Cold Spring & Breakneck Ridge",
                "location": "Breakneck Ridge Trailhead, Cold Spring, NY 10516",
                "website": "https://parks.ny.gov/parks/hudsonhighlands/details.aspx",
            },
            {
                "name": "Governors Island",
                "location": "10 South Street, Slip 7, New York, NY 10004",
                "website": "https://www.govisland.com/",
            },
            {
                "name": "QC NY Spa",
                "location": "112 Andes Road, New York, NY 10004",
                "website": "https://www.qcny.com/",
            },
            {
                "name": "Collective Retreats Governors Island",
                "location": "Governors Island, New York, NY 10004",
                "website": "https://www.collectiveretreats.com/retreat/governors-island/",
            },
            {
                "name": "Mohonk Preserve",
                "location": "3197 Route 44/55, Gardiner, NY 12525",
                "website": "https://www.mohonkpreserve.org/",
            },
            {
                "name": "Palisades Interstate Park",
                "location": "P.O. Box 155, Alpine, NJ 07620",
                "website": "https://njpalisades.org/",
            },
            {
                "name": "Jamaica Bay Wildlife Refuge",
                "location": "175-10 Cross Bay Boulevard, Queens, NY 11414",
                "website": "https://www.nps.gov/gate/index.htm",
            },
            {
                "name": "Storm King Art Center",
                "location": "New Windsor, NY",
                "website": "https://www.stormking.org/",
            },
        ],
    },
    "historic": {
        "excursion_type": "historic",
        "places": [
            {
                "name": "Dia Beacon",
                "location": "3 Beekman Street, Beacon, NY 12508",
                "website": "https://www.diaart.org/visit/visit-our-locations-sites/dia-beacon-beacon-united-states",
            },
            {
                "name": "Washington Irving's Sunnyside",
                "location": "West Sunnyside Lane, Tarrytown, NY",
                "website": "https://hudsonvalley.org/historic-sites/washington-irvings-sunnyside/",
            },
            {
                "name": "Lyndhurst Mansion",
                "location": "635 South Broadway, Tarrytown, NY 10591",
                "website": "https://lyndhurst.org/",
            },
            {
                "name": "Independence Hall",
                "location": "520 Chestnut Street, Philadelphia, PA 19106",
                "website": "https://www.nps.gov/inde/planyourvisit/independencehall.htm",
            },
            {
                "name": "Philadelphia Museum of Art",
                "location": "2600 Benjamin Franklin Parkway, Philadelphia, PA 19130",
                "website": "https://philamuseum.org/visit",
            },
            {
                "name": "Tenement Museum",
                "location": "103 Orchard Street, New York, NY 10002",
                "website": "https://www.tenement.org/",
            },
            {
                "name": "Save Ellis Island Hard Hat Tour",
                "location": "Ellis Island, New York Harbor, NY 10004",
                "website": "https://www.saveellisisland.org/tour/hard-hat-tours/page.html",
            },
            {
                "name": "Chateau Bloomberg",
                "location": "New York, NY",
                "website": "https://knowledge.kitchen/food-and-drink/ch%C3%A2teau-bloomberg/",
            },
            {
                "name": "Sleepy Hollow",
                "location": "Sleepy Hollow, NY",
                "website": "https://www.visitwestchesterny.com/",
            },
            {
                "name": "Kykuit Estate",
                "location": "Pocantico Hills, NY",
                "website": "https://www.rbf.org/",
            },
        ],
    },
    "coastal": {
        "excursion_type": "coastal",
        "places": [
            {
                "name": "Montauk Lighthouse",
                "location": "Montauk, NY",
                "website": "https://montaukhistoricalsociety.org/",
            },
            {
                "name": "Asbury Park Boardwalk",
                "location": "Asbury Park, NJ",
                "website": "https://www.apboardwalk.com/",
            },
            {
                "name": "New York Media Boat / Adventure Sightseeing",
                "location": "Chelsea Piers, Pier 59, New York, NY 10011",
                "website": "https://www.advsightseeing.com/",
            },
            {
                "name": "Secret Food Tours New York",
                "location": "Chinatown and Little Italy, Manhattan, NY",
                "website": "https://www.secretfoodtours.com/new-york/",
            },
        ],
    },
}

EXCURSION_ALIASES: Final[dict[str, str]] = {
    "beach": "coastal",
    "coastal": "coastal",
    "historic": "historic",
    "history": "historic",
    "nature": "nature",
    "outdoors": "nature",
}

def _normalize_excursion(category: str) -> str:
    key = " ".join(category.strip().lower().replace("-", " ").replace("_", " ").split())
    if key not in EXCURSION_ALIASES:
        raise ValueError(f"Unknown category '{category}'. Try: {', '.join(EXCURSION_OPTIONS)}")
    return EXCURSION_ALIASES[key]

def list_excursions(category: str) -> list[Excursion]:
    return [p.copy() for p in EXCURSION_OPTIONS[_normalize_excursion(category)]["places"]]


def find_excursion(category: str) -> Excursion:
    return random.choice(list_excursions(category))

def get_cafe(time: str) -> str:
    cafes = {
        "morning": [
            "Birch Coffee",
            "La Colombe",
            "Joe Coffee Company"
        ],
        "afternoon": [
            "Think Coffee",
            "787 Coffee",
            "Blue Bottle Coffee"
        ],
        "evening": [
            "Blank Street",
            "Cafe Lyria",
            "BlueStone Lane"
        ]
    }

    time = time.lower()
    if time not in cafes:
        return f"'{time}' is not valid. Try: morning, afternoon, evening."
    return random.choice(cafes[time])
