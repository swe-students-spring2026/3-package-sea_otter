import json
import re
import sys
import time
import urllib.request
from pathlib import Path

from bs4 import BeautifulSoup

BASE_URL = "https://guide.michelin.com/us/en/new-york-state/new-york/restaurants"
SITE_URL = "https://guide.michelin.com"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Upgrade-Insecure-Requests": "1",
}
DEFAULT_OUTPUT = Path(__file__).resolve().parents[1] / "pynyc" / "data" / "michelin_nyc.json"


def fetch_page_html(url: str) -> str:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8", errors="replace")


def parse_card(card) -> dict[str, str | None] | None:
    link_el = card.select_one("h3.card__menu-content--title a")
    if not link_el:
        return None

    name = link_el.get_text(strip=True)
    link = SITE_URL + link_el["href"]
    price = None
    cuisine = None

    info = card.select("div.card__menu-footer--score")
    if len(info) > 1:
        text = info[1].get_text(" ", strip=True)
        if "·" in text:
            left, right = [part.strip() for part in text.split("·", 1)]
            if left.startswith("$"):
                price = left
                cuisine = right
            else:
                cuisine = left
                if right.startswith("$"):
                    price = right
        elif text.startswith("$"):
            price = text
        else:
            cuisine = text

    return {"name": name, "cuisine": cuisine, "price": price, "url": link}


def has_more_pages(soup: BeautifulSoup) -> bool:
    heading = soup.find("h1")
    if not heading:
        return False

    text = heading.get_text(" ", strip=True)
    match = re.search(r"(\d+)\s*-\s*(\d+)\s+of\s+(\d+)\s+restaurants", text, re.I)
    if not match:
        return False

    shown_end = int(match.group(2))
    total = int(match.group(3))
    return shown_end < total


def scrape_restaurants() -> list[dict[str, str | None]]:
    restaurants: list[dict[str, str | None]] = []
    page = 1

    while True:
        url = BASE_URL if page == 1 else f"{BASE_URL}/page/{page}"
        print(f"fetching {url}", file=sys.stderr)

        html = fetch_page_html(url)
        soup = BeautifulSoup(html, "html.parser")
        cards = soup.select(
            "div.js-restaurant__list_items div.card__menu.selection-card.js-restaurant__list_item"
        )
        if not cards:
            cards = soup.select("div.card__menu.selection-card.js-restaurant__list_item")

        for card in cards:
            parsed = parse_card(card)
            if parsed:
                restaurants.append(parsed)

        if not has_more_pages(soup):
            break

        page += 1
        time.sleep(1)

    return restaurants


def main() -> None:
    payload = {"restaurants": scrape_restaurants()}
    output = json.dumps(payload, ensure_ascii=False, indent=2)
    output_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUTPUT
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as file:
        file.write(output)
        file.write("\n")
    print(f"wrote {output_path}", file=sys.stderr)


if __name__ == "__main__":
    main()