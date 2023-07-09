# Board Game Analysis

The goal of this project is to gather board game data from [Board Game Geek](https://boardgamegeek.com/) and use the game related information to gain insights about the games and possibly build a recommendation engine based on the data available. 

### **Board Game Data Gathering**
To gather the data, we use the Board Game Geek API to pull the game related information.  Information about the Board Game Geek API can be found [here](https://api.geekdo.com/xmlapi2).  To use the API, we will first have to gather game ids to build the API url.

We scrape the board game ids using the functions in the module titled scrape_game_ids.py and we save them in a csv file that we can use to build the API url.  We pulled the top 500 games from the website to start.  

After scraping the game ids, we can build and pull the data from the API.  To store the data we use a SQLite database.  The database schema can be found in the Documentation folder.

We currently have queries built to pull the top 5 years of game production order by the number of games published in that year, the top 5 most commonly used game mechanicisms, pulling games that have a particular mechanic, games that meet certain time constraints, age constraints, and player constraints. 


### **Executing Queries**

To run the queries, we can use the class SqlQueries to run the queries and then display them as a Pandas DataFrame. The below examples show how to pull a query without parameters and a query with parameters
```
sql_queries = SqlQueries(url)

# Query without Parameters
pd.DataFrame.from_dict(sql_queries.yearly_published_query())

# Query with Parameters
pd.DataFrame.from_dict(sql_queries.mechanic_games('Auction/Bidding'))
```


### **Tests**
Currently tests are built for 5 of the functions.  To run the tests just run the below from the command line in the portfolio directory.

```
pytest -v bgg_analysis/bgg_test/test.py
```


