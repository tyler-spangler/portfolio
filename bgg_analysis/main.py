"""
Module will populate database
"""
import pandas as pd
from api_call import (
    build_url,
    execute_api_call,
    parse_boardgame_data,
    parse_mechanic_data,
)
from data.database_utilities import write_to_database, read_yaml

title_id_df = pd.read_csv("bgg_analysis/game_title_id.csv")
database_filepath = read_yaml("bgg_analysis/data/database_configuration.yaml")[
    "bgg_database"
]["url"]


def load_boardgame_data():
    """
    Loads the boardgame data for the first 500 games in csv file
    """
    for start, stop in zip(range(0, 500, 100), range(100, 600, 100)):
        temp_url = build_url(100, title_id_df[start:stop])
        data_return = execute_api_call(temp_url)
        parsed_data = parse_boardgame_data(data_return)
        data_df = pd.DataFrame.from_dict(parsed_data, "columns")
        write_to_database(data_df, "boardgames", database_filepath)


def load_mechanic_data():
    """
    Loads the mechanic and mechanic_game data in database
    """
    loaded_mechanic_id = []
    for start, stop in zip(range(0, 500, 100), range(100, 600, 100)):
        temp_url = build_url(100, title_id_df[start:stop])
        data_return = execute_api_call(temp_url)
        parsed_data = parse_mechanic_data(data_return)
        data_df = pd.DataFrame.from_dict(parsed_data, "columns")
        mechanic_table_df = data_df[["id", "name"]].drop_duplicates()
        mechanic_table_df = mechanic_table_df[
            ~mechanic_table_df["id"].isin(loaded_mechanic_id)
        ]
        mechanic_game_df = data_df[["game_id", "id"]].rename(
            columns={"id": "mechanic_id"}
        )
        print(f"Writing games {start}-{stop} to database")
        write_to_database(mechanic_table_df, "mechanic", database_filepath)
        write_to_database(mechanic_game_df, "mechanic_game", database_filepath)
        loaded_mechanic_id.extend(mechanic_table_df["id"].to_list())
