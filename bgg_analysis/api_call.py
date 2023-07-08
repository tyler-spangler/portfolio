"""
Module will build and execute the API call
"""

import pandas as pd
import requests
import xmltodict

game_df = pd.read_csv("bgg_analysis/game_title_id.csv")


def build_url(n_games: int, games_df: pd.DataFrame) -> str:
    """
    Builds the url string based on a number of games requested
    Parameters
    ----------
    n_games: int
        Number of games to make the request for
    game_df: pd.DataFrame
        Dataframe with game_title and game_ids
    Returns
    -------
    str
        Returns the url to make the api request to
    """
    url_end = ""
    games_appended = 0
    for game_id in games_df["game_id"][:n_games].tolist():
        if games_appended == 0:
            url_end += f"{game_id}"
        else:
            url_end += f",{game_id}"

        games_appended += 1

    return f"https://api.geekdo.com/xmlapi/boardgame/{url_end}?comments=1"


def execute_api_call(api_url: str) -> dict:
    """
    Executes the get request on the generate url
    Paramters
    ---------
    url: str
        URL to call against the API
    Returns
    dict
        Dictionary of the xml response
    """

    try:
        response = requests.get(api_url, timeout=120)
        return xmltodict.parse(response.content)
    except requests.exceptions.RequestException as req_error:
        print(req_error)
        return None


def parse_boardgame_data(xml_dict: dict) -> dict:
    """
    Parse the returned xml into the board game table to load into the database
    Parameters
    ----------
    boardgame_dictionary: dict
        Dictionary to load the items into
    xml_dict: dict
        Dictionary of xml returned from the API
    Return
    ------
    dict
        The boardgame dictionary populated from the api data
    """
    boardgame_dictionary = {
        "game_id": [],
        "name": [],
        "min_players": [],
        "max_players": [],
        "min_playtime": [],
        "max_playtime": [],
        "age": [],
        "description": [],
        "year_published": [],
    }
    for game in xml_dict["boardgames"]["boardgame"]:
        # find the values and them to the dictionary
        boardgame_dictionary["game_id"].append(game["@objectid"])
        if isinstance(game["name"], list):
            for each_name in game["name"]:
                if "@primary" in list(each_name.keys()):
                    boardgame_dictionary["name"].append(each_name["#text"])
        else:
            boardgame_dictionary["name"].append(game["name"]["#text"])
        boardgame_dictionary["year_published"].append(game["yearpublished"])
        boardgame_dictionary["min_players"].append(game["minplayers"])
        boardgame_dictionary["max_players"].append(game["maxplayers"])
        boardgame_dictionary["min_playtime"].append(game["minplaytime"])
        boardgame_dictionary["max_playtime"].append(game["maxplaytime"])
        boardgame_dictionary["age"].append(game["age"])
        boardgame_dictionary["description"].append(game["description"])
    return boardgame_dictionary


def parse_mechanic_data(xml_dict: dict) -> dict:
    """
    Parses the xml data to pull out data regarding the game mechanics
    Parameters
    ----------
    xml_dict:
        Return value from calling the api
    Returns
    ---------
    dict
        Dictionary of parsed xml with game_id, mechanic id, and mechanic name
    """
    mechanic_data_dictionary = {"game_id": [], "id": [], "name": []}
    for game in xml_dict["boardgames"]["boardgame"]:
        game_id = game["@objectid"]
        if isinstance(game["boardgamemechanic"], list):
            for mechanic_dict in game["boardgamemechanic"]:
                mechanic_data_dictionary["game_id"].append(game_id)
                mechanic_data_dictionary["id"].append(mechanic_dict["@objectid"])
                mechanic_data_dictionary["name"].append(mechanic_dict["#text"])
        else:
            mechanic_data_dictionary["game_id"].append(game_id)
            mechanic_data_dictionary["id"].append(
                game["boardgamemechanic"]["@objectid"]
            )
            mechanic_data_dictionary["name"].append(game["boardgamemechanic"]["#text"])
    return mechanic_data_dictionary
