"""
Creates test database to test SqlQueries
"""

import pandas as pd
from database_utilities import (
    create_database,
    write_to_database,
)

DATABASE_LOCATION = "test_database.db"
boardgames_df = pd.DataFrame(
    {
        "game_id": [1, 3, 5],
        "name": ["Die Macher", "Samuri", "Acquire"],
        "min_players": [3, 2, 2],
        "max_players": [5, 4, 6],
        "max_playtime": [240, 60, 90],
        "age": [14, 10, 12],
        "description": [
            "Description Die Macher",
            "Description Samuri",
            "Description Acquire",
        ],
        "year_published": [1986, 1998, 1964],
    }
)

mechanic_df = pd.DataFrame(
    {
        "id": [2001, 2002, 2003],
        "name": ["Action Points", "Tile Placement", "Rock-Paper-Scissors"],
    }
)

mechanic_games_df = pd.DataFrame(
    {"mechanic_id": [2001, 2003, 2003, 2001, 2001], "game_id": [1, 1, 1, 3, 5]}
)

create_database(DATABASE_LOCATION)
write_to_database(boardgames_df, "boardgames", DATABASE_LOCATION)
write_to_database(mechanic_df, "mechanic", DATABASE_LOCATION)
write_to_database(mechanic_games_df, "mechanic_games", DATABASE_LOCATION)
