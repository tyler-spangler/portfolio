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
<<<<<<< HEAD
    for game_id in games_df["game_id"][:n_games].tolist():
        if games_appended == 0:
            url_end += f"{game_id}"
        else:
            url_end += f", {game_id}"
=======
    for _, row in games_df.iterrows():
        if games_appended == n_games:
            return f"https://api.geekdo.com/xmlapi/boardgame/{url_end}"

        if games_appended == 0:
            url_end += f"{row['game_id']}"
        else:
            url_end += f", {row['game_id']}"

>>>>>>> main
        games_appended += 1

    return f"https://api.geekdo.com/xmlapi/boardgame/{url_end}"


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
        response = requests.get(api_url, timeout=5)
        return xmltodict.parse(response.content)
    except requests.exceptions.RequestException as req_error:
        print(req_error)
        return None
