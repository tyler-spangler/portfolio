"""
This module will create and execute queries for metrics regarding the bgg data
"""
import sqlalchemy
from database_utilities import read_yaml


DATABASE_URL = read_yaml("bgg_analysis/data/database_configuration.yaml")[
    "bgg_database"
]["url"]


def execute_query(
    engine: sqlalchemy.engine.base.Engine, query: str, params: dict = None
) -> sqlalchemy.engine.cursor.CursorResult:
    """
    executes query without any parameters
    Parameters
    -----------
    engine: sqlAlchemy database engine
    query: str
        Query to execute
    Returns
    -------
    Query results
    """
    with engine.connect() as conn:
        query_text = sqlalchemy.text(query)
        results = conn.execute(query_text, params)
    return results


class SqlQueries:
    """
    Defines and executes sql queries for bgg database
    Parameters
    ----------
    url: str
        URL for the database
    """

    def __init__(self, url):
        self.engine = sqlalchemy.create_engine(f"sqlite:///{url}")

    def yearly_published_query(self) -> dict:
        """
        Queries the database to find the top 5 years of game production
        Returns
        -------
        dict
            Dictionary of query results
        """
        yearly_published_query = """
        SELECT year_published
            , count(game_id) AS num_games
        FROM boardgames
        GROUP BY year_published
        ORDER BY 2 desc
        LIMIT 5
        """
        results = execute_query(self.engine, yearly_published_query)

        return [row._asdict() for row in results.fetchall()]

    def most_used_mechanics(self) -> dict:
        """
        Queries the database to show the top five mechanics
        Returns
        -------
        dict
            Dictionary of results
        """
        top_five_mechanics = """
        SELECT mechanic.name
            , count(mechanic_game.mechanic_id)
        FROM mechanic
        JOIN mechanic_game on mechanic_game.mechanic_id = mechanic.id
        GROUP BY mechanic.name
        ORDER by 2 desc
        LIMIT 5
        """
        results = execute_query(self, top_five_mechanics)
        return [row._asdict() for row in results.fetchall()]

    def mechanic_games(self, mechanic_name: str) -> dict:
        """
        Queries the database to find games and descriptions with the specified mechanic
        Parameters
        ----------
        mechanic_name: str
            Name of the mechanic to search for
        Returns
        -------
        dict
            Dictionary of results
        """
        games_for_given_mechanic = """
        SELECT boardgames.name
            , mechanic.name
            , boardgames.description
        FROM boardgames
        JOIN mechanic_game on mechanic_game.game_id = boardgames.game_id
        JOIN mechanic on mechanic.id = mechanic_game.mechanic_id
        WHERE mechanic.name = :mechanic_name
        """
        results = execute_query(
            self.engine,
            games_for_given_mechanic,
            params={"mechanic_name": mechanic_name},
        )
        return [row._asdict() for row in results.fetchall()]

    def age_range_games(self, min_age: int, max_age: int) -> dict:
        """
        Queries database to find games in specified age range
        Parameters
        -----------
        min_age: int
            Minimum age to search for
        max_age: int
            Maximum age to search for
        Returns
        -------
        dict
            Dictionary of query results
        """
        age_range_games = """
        SELECT boardgames.name as game_name
            , boardgames.age
            , boardgames.description
        FROM boardgames
        WHERE boardgames.age BETWEEN :min_age AND :max_age
        """
        results = execute_query(
            self.engine,
            age_range_games,
            params={"min_age": min_age, "max_age": max_age},
        )
        return [row._asdict() for row in results.fetchall()]

    def game_time_limits(self, max_time: int) -> dict:
        """
        Queries database for games that are under a certain max playtime
        Parameters
        ----------
        max_time: int
            Max time to search for
        Returns
        -------
        dict
            Dictionary of results
        """
        time_limits = """
        SELECT boardgames.name
            , boardgames.min_playtime || '-' || boardgames.max_playtime AS time_range
            , boardgames.description
        FROM boardgames
        WHERE boardgames.max_playtime < :max_playtime
        """
        results = execute_query(
            self.engine, time_limits, params={"max_playtime": max_time}
        )
        return [row._asdict() for row in results.fetchall()]

    def game_for_players(self, min_players: int) -> dict:
        """
        Queries database for games for a min amount of players
        """
        num_players = """
        SELECT boardgames.name
           , boardgames.min_players || '-' || boardgames.max_players AS player_range
           , boardgames.description
        FROM boardgames
        WHERE boardgames.min_players > :min_players
        """
        results = execute_query(
            self.engine, num_players, params={"min_players": min_players}
        )
        return [row._asdict() for row in results.fetchall()]
