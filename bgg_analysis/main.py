"""
Module will populate database
"""
import pandas as pd
from api_call import build_url, execute_api_call, parse_boardgame_data
from data.database_utilities import write_to_database, read_yaml

title_id_df = pd.read_csv("bgg_analysis/game_title_id.csv")
database_filepath = read_yaml("bgg_analysis/data/database_configuration.yaml")[
    "bgg_database"
]["url"]

for start, stop in zip(range(0, 500, 100), range(100, 600, 100)):
    temp_url = build_url(100, title_id_df[start:stop])
    data_return = execute_api_call(temp_url)
    parsed_data = parse_boardgame_data(data_return)
    data_df = pd.DataFrame.from_dict(parsed_data, "columns")
    write_to_database(data_df, "boardgames", database_filepath)
