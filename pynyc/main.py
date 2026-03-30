from pynyc import (
    find_activity,
    find_excursion,
    find_nightlife_activity,
    find_restaurant,
    list_excursions,
    list_nightlife_places,
)

def main() -> None:
    print("pynyc demo")
    print("-" * 40)

    restaurant = find_restaurant("American", 18)
    activity = find_activity("sunny")

    nightlife_places = list_nightlife_places("dancing")
    nightlife_pick = find_nightlife_activity("karaoke")

    excursion_list = list_excursions("nature")
    excursion_pick = find_excursion("historic")

    print(f"Restaurant suggestion: {restaurant}")
    print(f"Activity suggestion: {activity}")

    print("Nightlife options (dancing):")
    for place in nightlife_places:
        print(f"- {place['name']} -> {place['website']}")

    print(
        "Nightlife pick (karaoke): "
        f"{nightlife_pick['name']} [{nightlife_pick['activity_type']}] -> {nightlife_pick['website']}"
    )

    print("Excursion options (nature):")
    for spot in excursion_list:
        print(f"- {spot['name']} ({spot['location']}) -> {spot['website']}")

    print(
        "Excursion pick (historic): "
        f"{excursion_pick['name']} ({excursion_pick['location']}) -> {excursion_pick['website']}"
    )
