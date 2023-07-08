"""
Module contains functions for creating and updating database
"""
import sqlite3 as sql
import yaml
import pandas as pd


def create_database(file_path: str):
    """
    Creates database at the provided location
    Parameters
    -----------
    file_path: str
        File path to where database should reside
    """
    database_connection = sql.connect(file_path)
    database_cursor = database_connection.cursor()

    database_cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS boardgames ([game_id] INTEGER PRIMARY KEY, [name] TEXT, 
        [min_players] INTEGER, [max_players] INTEGER, [min_playtime] INTEGER, 
        [max_playtime] INTEGER, [age] INTEGER, [description] TEXT, [year_published] INTEGER)
        """
    )

    database_cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS publishers ([id] INTEGER PRIMARY KEY, 
        [name] TEXT)
        """
    )

    database_cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS publishers_games(
        game_id INTEGER, publisher_id INTEGER,
        FOREIGN KEY(game_id) REFERENCES boardgame(gamee_id),
        FOREIGN KEY(publisher_id) REFERENCES publishers(id)
        )
        """
    )
    database_cursor.execute(
        "CREATE TABLE IF NOT EXISTS mechanic ([id] INTEGER PRIMARY KEY, [name] TEXT)"
    )
    database_cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS mechanic_game ([mechanic_id] INTEGER, [game_id] INTEGER,
        FOREIGN KEY(game_id) REFERENCES boardgames(game_id), 
        FOREIGN KEY(mechanic_id) REFERENCES mechanic(id))
        """
    )

    database_connection.commit()


def write_to_database(
    data_to_write: pd.DataFrame, table_name: str, database_location: str
) -> None:
    """
    Writes a dataframe to the provided table
    Parameters
    -----------
    data_to_write: pd.DataFrame
        Dataframe to write to the table
    table_name: str
        Which table in database to write to
    database_location: str
        Location of database
    """
    database_connection = sql.connect(database_location)
    data_to_write.to_sql(
        table_name, database_connection, if_exists="append", index=False
    )


def read_yaml(filepath: str) -> dict:
    """
    Reads the configuration file and returns the dictionary
    Parameters
    -----------
    filepath: str
        Filepath to the configuration file
    Returns
    --------
    dict:
        Dictionary containing the filepath to the database
    """
    with open(filepath, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)
    return config


def reset_table(table_name: str):
    """
    resets table by deleting all the rows
    """
    database_path = read_yaml("bgg_analysis/data/database_configuration.yaml")[
        "bgg_database"
    ]["url"]
    database_conn = sql.connect(database_path)
    database_cursor = database_conn.cursor()
    database_cursor.execute(f"DELETE FROM {table_name}")
    database_conn.commit()
    database_conn.close()


reset_table("mechanic")
reset_table("mechanic_game")
