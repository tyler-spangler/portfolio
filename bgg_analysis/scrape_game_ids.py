"""
Scrapes bgg to get game ids. Starts by only scraping top 200 games
"""
import re
from typing import Union
import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_game_urls(url: str) -> set:
    """
    Scrapes the html from the provided url
    Parameters:
    -----------
    url: str
        URL to ge the html for
    Returns:
    ----------
    html
    """
    page_content = requests.get(url, timeout=5)
    parsed_content = BeautifulSoup(page_content.text, "html.parser")
    game_urls = set()
    for game_link in parsed_content.find_all(
        "a", attrs={"href": re.compile("^/boardgame/")}
    ):
        game_urls.add(game_link["href"])
    return game_urls


def get_title_id(game_urls: Union[set, list]) -> pd.DataFrame:
    """
    Parses out the game url endings
    Parameters
    -----------
    game_urls: set
        A set of game urls if only scraping one url or list of sets if scraping many urls
    Returns
    --------
    pd.DataFrame
        Dataframe with game ids and titles
    """
    game_title = []
    game_id = []
    for url in game_urls:
        url_list = url.split("/")
        game_title.append(url_list[3])
        game_id.append(url_list[2])
    return pd.DataFrame({"game_title": game_title, "game_id": game_id})


# loop through and get first 5 pages (top 500 games)
scrape_url_list = ["https://boardgamegeek.com/browse/boardgame"] + [
    f"https://boardgamegeek.com/browse/boardgame/page/{i+1}" for i in range(1, 5)
]
temp_list = []
for temp_url in scrape_url_list:
    temp_list.append(get_game_urls(temp_url))

game_url_list = [game_url for set_list in temp_list for game_url in set_list]
game_id_df = get_title_id(game_urls=game_url_list)

# game_id_df.to_csv("game_title_id.csv")
