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
    for _, row in games_df.iterrows():
        if games_appended == 0:
            url_end += f"{row['game_id']}"

        url_end += f", {row['game_id']}"

        if games_appended == n_games:
            return f"https://api.geekdo.com/xmlapi/boardgame/{url_end}"

        games_appended += 1


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
    response = requests.get(api_url, timeout=5)
    if response.status_code == 200:
        return xmltodict.parse(response.content)
    return response.status_code


url = build_url(1, games_df=game_df)
x = execute_api_call(url)
print(x)
d = {
    "boardgames": {
        "@termsofuse": "https://boardgamegeek.com/xmlapi/termsofuse",
        "boardgame": [
            {
                "@objectid": "161533",
                "yearpublished": "2017",
                "minplayers": "1",
                "maxplayers": "4",
                "playingtime": "120",
                "minplaytime": "60",
                "maxplaytime": "120",
                "age": "12",
                "name": [
                    {"@primary": "true", "@sortindex": "1", "#text": "Lisboa"},
                    {"@sortindex": "1", "#text": "Лиссабон"},
                    {"@sortindex": "1", "#text": "里斯本"},
                    {"@sortindex": "1", "#text": "리스보아"},
                ],
                "description": "Lisboa is a game about the reconstruction of Lisboa after the great earthquake of 1755.<br/><br/>On November 1, 1755, Lisbon suffered an earthquake of an estimated magnitude of 8.5&ndash;9.0, followed by a tsunami and three days of fires. The city was almost totally destroyed. The Marques of Pombal &mdash; Sebasti&atilde;o Jos&eacute; de Carvalho e Melo &mdash; was the then Minister of Foreign Affairs and the King put him in charge of the reconstruction of Lisbon. The Marques of Pombal gathered a team of engineers and architects and you, the players, are members of the nobility; members who will use your influence in the reconstruction and business development of the new city. You will work with the architects to build Lisbon anew, with the Marquis to develop commerce and with the King to open all the buildings, but the true reason you do all this is not for greatness or fame or even fortune, but for the most important thing of all in that time: wigs.<br/><br/>Lisboa is played on a real map of downtown Lisbon. During the planning of the downtown project, the type of business permitted in each street was previously determined. The economic motor is driven by the wealth of the royal treasure and this treasure is controlled by player actions during the game, making each game a totally different experience. The game ends after a fixed number of rounds and whoever gathers the most wigs by the end of the game wins.<br/><br/>Lisboa is played in rounds. Each round, all players play one turn. They may place one card on their display or replace one card from this display. During the game, players schedule hearings to get character favors, such as commerce, construction, and openings. The iconic buildings score the stores and stores provide income to the players. Players need to manage influence, construction licenses, store permits, church power, workers and money, with the workers' cost being dependent on the prestige of the players.<br/><br/>",
                "thumbnail": "https://cf.geekdo-images.com/OrHS8_a1CqSGiXeTfCk0Wg__thumb/img/ZBTT0qZcD5HMFlhFN7PLMe6zXvg=/fit-in/200x150/filters:strip_icc()/pic3209553.jpg",
                "image": "https://cf.geekdo-images.com/OrHS8_a1CqSGiXeTfCk0Wg__original/img/hVArRkZYHiPTGTfi0DPR58i4o44=/0x0/filters:format(jpeg)/pic3209553.jpg",
                "boardgamepublisher": [
                    {"@objectid": "597", "#text": "Eagle-Gryphon Games"},
                    {"@objectid": "38809", "#text": "Angry Lion Games"},
                    {"@objectid": "6194", "#text": "Delta Vision Publishing"},
                    {"@objectid": "7251", "#text": "Giochix.it"},
                    {"@objectid": "10562", "#text": "hobbity.eu"},
                    {"@objectid": "34801", "#text": "Lavka Games"},
                    {"@objectid": "30677", "#text": "Maldito Games"},
                    {"@objectid": "35035", "#text": "Mandala Jogos"},
                    {"@objectid": "41423", "#text": "TLAMA games"},
                    {"@objectid": "8147", "#text": "YOKA Games"},
                ],
                "boardgamehonor": [
                    {
                        "@objectid": "61811",
                        "#text": "2017 Board Game Quest Awards Best Production Values Nominee",
                    },
                    {
                        "@objectid": "61812",
                        "#text": "2017 Board Game Quest Awards Best Strategy/Euro Game Nominee",
                    },
                    {
                        "@objectid": "61820",
                        "#text": "2017 Board Game Quest Awards Best Strategy/Euro Game Winner",
                    },
                    {
                        "@objectid": "61814",
                        "#text": "2017 Board Game Quest Awards Game of the Year Nominee",
                    },
                    {
                        "@objectid": "46984",
                        "#text": "2017 Cardboard Republic Tactician Laurel Nominee",
                    },
                    {
                        "@objectid": "47798",
                        "#text": "2017 Cardboard Republic Tactician Laurel Winner",
                    },
                    {
                        "@objectid": "47451",
                        "#text": "2017 Golden Geek Best Board Game Artwork & Presentation Nominee",
                    },
                    {
                        "@objectid": "47472",
                        "#text": "2017 Golden Geek Best Strategy Board Game Nominee",
                    },
                    {
                        "@objectid": "47432",
                        "#text": "2017 Golden Geek Board Game of the Year Nominee",
                    },
                    {"@objectid": "48768", "#text": "2017 Meeples' Choice Nominee"},
                    {
                        "@objectid": "64683",
                        "#text": "2017 The Golden Elephant Award Best Heavy Board Game Winner",
                    },
                    {
                        "@objectid": "64682",
                        "#text": "2017 The Golden Elephant Award Finalist",
                    },
                    {
                        "@objectid": "64684",
                        "#text": "2017 The Golden Elephant Award People's Choice Winner",
                    },
                    {
                        "@objectid": "61699",
                        "#text": "2018 5 Seasons Best Portuguese Strategy Game Nominee",
                    },
                    {
                        "@objectid": "61706",
                        "#text": "2018 5 Seasons Best Portuguese Strategy Game Winner",
                    },
                    {"@objectid": "58030", "#text": "2018 Jogo do Ano Nominee"},
                    {"@objectid": "58028", "#text": "2018 Jogo do Ano Winner"},
                    {
                        "@objectid": "74281",
                        "#text": "2018 Kanga Best Gameplay Finalist",
                    },
                    {"@objectid": "74284", "#text": "2018 Kanga Best Gameplay Winner"},
                    {"@objectid": "74282", "#text": "2018 Kanga Best Visuals Finalist"},
                    {
                        "@objectid": "74280",
                        "#text": "2018 Kanga Game of the Year Finalist",
                    },
                ],
                "boardgamemechanic": [
                    {"@objectid": "2080", "#text": "Area Majority / Influence"},
                    {"@objectid": "2040", "#text": "Hand Management"},
                    {"@objectid": "2041", "#text": "Open Drafting"},
                    {"@objectid": "2819", "#text": "Solo / Solitaire Game"},
                    {"@objectid": "2002", "#text": "Tile Placement"},
                ],
                "boardgamepodcastepisode": [
                    {
                        "@objectid": "208915",
                        "#text": "BGA Episode 123 - The BGG Hotness Review (Origins Edition)",
                    },
                    {
                        "@objectid": "213549",
                        "#text": "clp057 – cubelove podcast – Lisboa, Spirit of the Rules, 2007",
                    },
                    {
                        "@objectid": "193181",
                        "#text": "Cult of the New Board Game Podcast Episode 033 – Great Western Trail vs The Oracle of Delphi",
                    },
                    {
                        "@objectid": "252168",
                        "#text": "Ep 070 &ndash; 3rd Anniversary Special &amp; Tournament to the Death!!!",
                    },
                    {
                        "@objectid": "380489",
                        "#text": "Ep.84 Lisboa, Enjoying the Experience, and 2021 Achievements",
                    },
                    {
                        "@objectid": "233980",
                        "#text": "Episode 10 - Holy Reiner Knizia, We Made It To Double Digits!",
                    },
                    {
                        "@objectid": "211599",
                        "#text": "Episode 113 -- This Guy, That Guy, and the Other",
                    },
                    {
                        "@objectid": "227438",
                        "#text": "Episode 114- Lisboa &amp; 2018 Board Gaming Predictions/Resolutions",
                    },
                    {
                        "@objectid": "446223",
                        "#text": "Episode 12: Top 5 BGG 100 Games We Want to Play",
                    },
                    {
                        "@objectid": "214896",
                        "#text": "Episode 14 - To Budget Or Not To Budget, That Is The Question",
                    },
                    {"@objectid": "391320", "#text": "Episode 145 :: Joy of the Stick"},
                    {"@objectid": "219512", "#text": "Episode 15 - Cabin In The Woods"},
                    {"@objectid": "358218", "#text": "Episode 152: Pit Spit"},
                    {
                        "@objectid": "170839",
                        "#text": "Episode 16 - Looking Ahead to 2016",
                    },
                    {
                        "@objectid": "292240",
                        "#text": "Episode 17: Lisboa, Planet, Copenhagen - Association Station - Top 5 Games with the Best Artwork",
                    },
                    {
                        "@objectid": "472096",
                        "#text": "Episode 23: Discovering the Lacerdaverse (Vital Lacerda Games)",
                    },
                    {
                        "@objectid": "322197",
                        "#text": "Episode 24 – Catching Up, Lisboa, &amp; Downforce",
                    },
                    {
                        "@objectid": "465586",
                        "#text": "Episode 28: Top 30 Countdown, Part III (10-1)",
                    },
                    {
                        "@objectid": "196138",
                        "#text": "Episode 39 - Our Most Anticipated Games in 2017",
                    },
                    {
                        "@objectid": "262250",
                        "#text": "Episode 46: Mr. Jack, Lords of Waterdeep, Apocrypha, Lisboa, KLASK",
                    },
                    {
                        "@objectid": "430924",
                        "#text": "Episode 4: Top 5 Shelf of Shame Games",
                    },
                    {
                        "@objectid": "211990",
                        "#text": "Episode 50 - Gen Con 2017 Two-Player Preview",
                    },
                    {
                        "@objectid": "227996",
                        "#text": "Episode 66 :: Charterstone Review + Best Board Games of 2017",
                    },
                    {
                        "@objectid": "475193",
                        "#text": "Expansion Pack: Birthday Boardgame Battleground - 2022 Turbo Edition",
                    },
                    {
                        "@objectid": "227730",
                        "#text": "It’s Our Turn! Episode #45: Ancient Era Games",
                    },
                    {"@objectid": "219335", "#text": "MHGG Review - Lisboa"},
                    {
                        "@objectid": "299879",
                        "#text": "Out of the Dust Ep46 - Terraforming Mars",
                    },
                    {"@objectid": "228920", "#text": "Review Episode 07 - Lisboa"},
                    {
                        "@objectid": "193133",
                        "#text": "The Dice Men Cometh – Episode 143",
                    },
                    {
                        "@objectid": "213351",
                        "#text": 'The Good The Board and The Playstyle?: Episode 129 "Playstyle"',
                    },
                    {
                        "@objectid": "211565",
                        "#text": "Vox Republica 148: Combating The Pile of Shame",
                    },
                    {
                        "@objectid": "220708",
                        "#text": "Vox Republica 155: Charitable Gaming",
                    },
                    {
                        "@objectid": "157900",
                        "#text": "What Did You Play This Week Podcast Thing Week 37!!!",
                    },
                    {
                        "@objectid": "220091",
                        "#text": "Winning The One’s Affection – Ep. 1",
                    },
                ],
                "boardgameversion": [
                    {"@objectid": "627704", "#text": "Chinese edition"},
                    {
                        "@objectid": "642938",
                        "#text": "Czech/English Deluxe Kickstarter edition",
                    },
                    {"@objectid": "395932", "#text": "English deluxe edition"},
                    {"@objectid": "244339", "#text": "English standard edition"},
                    {"@objectid": "595357", "#text": "French deluxe edition"},
                    {"@objectid": "456758", "#text": "German deluxe edition"},
                    {"@objectid": "612861", "#text": "Hungarian edition"},
                    {"@objectid": "370519", "#text": "Italian edition"},
                    {"@objectid": "498827", "#text": "Korean edition"},
                    {"@objectid": "361341", "#text": "Polish edition"},
                    {"@objectid": "372724", "#text": "Portuguese edition"},
                    {"@objectid": "578441", "#text": "Russian deluxe edition"},
                    {"@objectid": "558265", "#text": "Spanish edition"},
                ],
                "boardgamefamily": [
                    {"@objectid": "43603", "#text": "Cities: Lisbon (Portugal)"},
                    {"@objectid": "65191", "#text": "Components: Multi-Use Cards"},
                    {"@objectid": "5614", "#text": "Country: Portugal"},
                    {"@objectid": "25292", "#text": "Crowdfunding: Giochistarter"},
                    {"@objectid": "8374", "#text": "Crowdfunding: Kickstarter"},
                    {"@objectid": "22135", "#text": "Crowdfunding: Spieleschmiede"},
                    {
                        "@objectid": "70948",
                        "#text": "Digital Implementations: Tabletopia",
                    },
                    {"@objectid": "78680", "#text": "Misc: Made by Panda"},
                    {
                        "@objectid": "5666",
                        "#text": "Players: Games with Solitaire Rules",
                    },
                    {"@objectid": "73380", "#text": "Theme: Earthquakes"},
                ],
                "boardgamecategory": [
                    {"@objectid": "1029", "#text": "City Building"},
                    {"@objectid": "1021", "#text": "Economic"},
                    {"@objectid": "1088", "#text": "Industry / Manufacturing"},
                    {"@objectid": "1001", "#text": "Political"},
                ],
                "boardgamedeveloper": [
                    {"@objectid": "56863", "#text": "Paul Incao"},
                    {"@objectid": "112575", "#text": "Julián Pombo"},
                ],
                "boardgamedesigner": {"@objectid": "12396", "#text": "Vital Lacerda"},
                "boardgamesolodesigner": [
                    {"@objectid": "12396", "#text": "Vital Lacerda"},
                    {"@objectid": "112575", "#text": "Julián Pombo"},
                ],
                "boardgameaccessory": [
                    {"@objectid": "232915", "#text": "Lisboa: Heavy Cardboard Promo"},
                    {"@objectid": "237375", "#text": "Lisboa: Metal Coins"},
                    {"@objectid": "290603", "#text": "Lisboa: Upgrade Pack"},
                ],
                "boardgameexpansion": {
                    "@objectid": "301771",
                    "#text": "Lisboa: Queen Variant",
                },
                "boardgameimplementation": {
                    "@objectid": "262477",
                    "#text": "Mercado de Lisboa",
                },
                "boardgameartist": {"@objectid": "64844", "#text": "Ian O'Toole"},
                "boardgamegraphicdesigner": {
                    "@objectid": "64844",
                    "#text": "Ian O'Toole",
                },
                "boardgamesubdomain": {"@objectid": "5497", "#text": "Strategy Games"},
                "poll": [
                    {
                        "@name": "suggested_numplayers",
                        "@title": "User Suggested Number of Players",
                        "@totalvotes": "259",
                        "results": [
                            {
                                "@numplayers": "1",
                                "result": [
                                    {"@value": "Best", "@numvotes": "5"},
                                    {"@value": "Recommended", "@numvotes": "88"},
                                    {"@value": "Not Recommended", "@numvotes": "44"},
                                ],
                            },
                            {
                                "@numplayers": "2",
                                "result": [
                                    {"@value": "Best", "@numvotes": "44"},
                                    {"@value": "Recommended", "@numvotes": "139"},
                                    {"@value": "Not Recommended", "@numvotes": "20"},
                                ],
                            },
                            {
                                "@numplayers": "3",
                                "result": [
                                    {"@value": "Best", "@numvotes": "154"},
                                    {"@value": "Recommended", "@numvotes": "50"},
                                    {"@value": "Not Recommended", "@numvotes": "2"},
                                ],
                            },
                            {
                                "@numplayers": "4",
                                "result": [
                                    {"@value": "Best", "@numvotes": "48"},
                                    {"@value": "Recommended", "@numvotes": "115"},
                                    {"@value": "Not Recommended", "@numvotes": "30"},
                                ],
                            },
                            {
                                "@numplayers": "4+",
                                "result": [
                                    {"@value": "Best", "@numvotes": "0"},
                                    {"@value": "Recommended", "@numvotes": "0"},
                                    {"@value": "Not Recommended", "@numvotes": "85"},
                                ],
                            },
                        ],
                    },
                    {
                        "@name": "language_dependence",
                        "@title": "Language Dependence",
                        "@totalvotes": "14",
                        "results": {
                            "result": [
                                {
                                    "@level": "1",
                                    "@value": "No necessary in-game text",
                                    "@numvotes": "10",
                                },
                                {
                                    "@level": "2",
                                    "@value": "Some necessary text - easily memorized or small crib sheet",
                                    "@numvotes": "4",
                                },
                                {
                                    "@level": "3",
                                    "@value": "Moderate in-game text - needs crib sheet or paste ups",
                                    "@numvotes": "0",
                                },
                                {
                                    "@level": "4",
                                    "@value": "Extensive use of text - massive conversion needed to be playable",
                                    "@numvotes": "0",
                                },
                                {
                                    "@level": "5",
                                    "@value": "Unplayable in another language",
                                    "@numvotes": "0",
                                },
                            ]
                        },
                    },
                    {
                        "@name": "suggested_playerage",
                        "@title": "User Suggested Player Age",
                        "@totalvotes": "42",
                        "results": {
                            "result": [
                                {"@value": "2", "@numvotes": "0"},
                                {"@value": "3", "@numvotes": "0"},
                                {"@value": "4", "@numvotes": "0"},
                                {"@value": "5", "@numvotes": "0"},
                                {"@value": "6", "@numvotes": "0"},
                                {"@value": "8", "@numvotes": "0"},
                                {"@value": "10", "@numvotes": "1"},
                                {"@value": "12", "@numvotes": "8"},
                                {"@value": "14", "@numvotes": "19"},
                                {"@value": "16", "@numvotes": "12"},
                                {"@value": "18", "@numvotes": "2"},
                                {"@value": "21 and up", "@numvotes": "0"},
                            ]
                        },
                    },
                ],
            },
            {
                "@objectid": "161533",
                "yearpublished": "2017",
                "minplayers": "1",
                "maxplayers": "4",
                "playingtime": "120",
                "minplaytime": "60",
                "maxplaytime": "120",
                "age": "12",
                "name": [
                    {"@primary": "true", "@sortindex": "1", "#text": "Lisboa"},
                    {"@sortindex": "1", "#text": "Лиссабон"},
                    {"@sortindex": "1", "#text": "里斯本"},
                    {"@sortindex": "1", "#text": "리스보아"},
                ],
                "description": "This page does not exist. You can edit this page to create it.",
                "thumbnail": "https://cf.geekdo-images.com/OrHS8_a1CqSGiXeTfCk0Wg__thumb/img/ZBTT0qZcD5HMFlhFN7PLMe6zXvg=/fit-in/200x150/filters:strip_icc()/pic3209553.jpg",
                "image": "https://cf.geekdo-images.com/OrHS8_a1CqSGiXeTfCk0Wg__original/img/hVArRkZYHiPTGTfi0DPR58i4o44=/0x0/filters:format(jpeg)/pic3209553.jpg",
                "boardgamepublisher": [
                    {"@objectid": "597", "#text": "Eagle-Gryphon Games"},
                    {"@objectid": "38809", "#text": "Angry Lion Games"},
                    {"@objectid": "6194", "#text": "Delta Vision Publishing"},
                    {"@objectid": "7251", "#text": "Giochix.it"},
                    {"@objectid": "10562", "#text": "hobbity.eu"},
                    {"@objectid": "34801", "#text": "Lavka Games"},
                    {"@objectid": "30677", "#text": "Maldito Games"},
                    {"@objectid": "35035", "#text": "Mandala Jogos"},
                    {"@objectid": "41423", "#text": "TLAMA games"},
                    {"@objectid": "8147", "#text": "YOKA Games"},
                ],
                "boardgamehonor": [
                    {
                        "@objectid": "61811",
                        "#text": "2017 Board Game Quest Awards Best Production Values Nominee",
                    },
                    {
                        "@objectid": "61812",
                        "#text": "2017 Board Game Quest Awards Best Strategy/Euro Game Nominee",
                    },
                    {
                        "@objectid": "61820",
                        "#text": "2017 Board Game Quest Awards Best Strategy/Euro Game Winner",
                    },
                    {
                        "@objectid": "61814",
                        "#text": "2017 Board Game Quest Awards Game of the Year Nominee",
                    },
                    {
                        "@objectid": "46984",
                        "#text": "2017 Cardboard Republic Tactician Laurel Nominee",
                    },
                    {
                        "@objectid": "47798",
                        "#text": "2017 Cardboard Republic Tactician Laurel Winner",
                    },
                    {
                        "@objectid": "47451",
                        "#text": "2017 Golden Geek Best Board Game Artwork & Presentation Nominee",
                    },
                    {
                        "@objectid": "47472",
                        "#text": "2017 Golden Geek Best Strategy Board Game Nominee",
                    },
                    {
                        "@objectid": "47432",
                        "#text": "2017 Golden Geek Board Game of the Year Nominee",
                    },
                    {"@objectid": "48768", "#text": "2017 Meeples' Choice Nominee"},
                    {
                        "@objectid": "64683",
                        "#text": "2017 The Golden Elephant Award Best Heavy Board Game Winner",
                    },
                    {
                        "@objectid": "64682",
                        "#text": "2017 The Golden Elephant Award Finalist",
                    },
                    {
                        "@objectid": "64684",
                        "#text": "2017 The Golden Elephant Award People's Choice Winner",
                    },
                    {
                        "@objectid": "61699",
                        "#text": "2018 5 Seasons Best Portuguese Strategy Game Nominee",
                    },
                    {
                        "@objectid": "61706",
                        "#text": "2018 5 Seasons Best Portuguese Strategy Game Winner",
                    },
                    {"@objectid": "58030", "#text": "2018 Jogo do Ano Nominee"},
                    {"@objectid": "58028", "#text": "2018 Jogo do Ano Winner"},
                    {
                        "@objectid": "74281",
                        "#text": "2018 Kanga Best Gameplay Finalist",
                    },
                    {"@objectid": "74284", "#text": "2018 Kanga Best Gameplay Winner"},
                    {"@objectid": "74282", "#text": "2018 Kanga Best Visuals Finalist"},
                    {
                        "@objectid": "74280",
                        "#text": "2018 Kanga Game of the Year Finalist",
                    },
                ],
                "boardgamemechanic": [
                    {"@objectid": "2080", "#text": "Area Majority / Influence"},
                    {"@objectid": "2040", "#text": "Hand Management"},
                    {"@objectid": "2041", "#text": "Open Drafting"},
                    {"@objectid": "2819", "#text": "Solo / Solitaire Game"},
                    {"@objectid": "2002", "#text": "Tile Placement"},
                ],
                "boardgamepodcastepisode": [
                    {
                        "@objectid": "208915",
                        "#text": "BGA Episode 123 - The BGG Hotness Review (Origins Edition)",
                    },
                    {
                        "@objectid": "213549",
                        "#text": "clp057 – cubelove podcast – Lisboa, Spirit of the Rules, 2007",
                    },
                    {
                        "@objectid": "193181",
                        "#text": "Cult of the New Board Game Podcast Episode 033 – Great Western Trail vs The Oracle of Delphi",
                    },
                    {
                        "@objectid": "252168",
                        "#text": "Ep 070 &ndash; 3rd Anniversary Special &amp; Tournament to the Death!!!",
                    },
                    {
                        "@objectid": "380489",
                        "#text": "Ep.84 Lisboa, Enjoying the Experience, and 2021 Achievements",
                    },
                    {
                        "@objectid": "233980",
                        "#text": "Episode 10 - Holy Reiner Knizia, We Made It To Double Digits!",
                    },
                    {
                        "@objectid": "211599",
                        "#text": "Episode 113 -- This Guy, That Guy, and the Other",
                    },
                    {
                        "@objectid": "227438",
                        "#text": "Episode 114- Lisboa &amp; 2018 Board Gaming Predictions/Resolutions",
                    },
                    {
                        "@objectid": "446223",
                        "#text": "Episode 12: Top 5 BGG 100 Games We Want to Play",
                    },
                    {
                        "@objectid": "214896",
                        "#text": "Episode 14 - To Budget Or Not To Budget, That Is The Question",
                    },
                    {"@objectid": "391320", "#text": "Episode 145 :: Joy of the Stick"},
                    {"@objectid": "219512", "#text": "Episode 15 - Cabin In The Woods"},
                    {"@objectid": "358218", "#text": "Episode 152: Pit Spit"},
                    {
                        "@objectid": "170839",
                        "#text": "Episode 16 - Looking Ahead to 2016",
                    },
                    {
                        "@objectid": "292240",
                        "#text": "Episode 17: Lisboa, Planet, Copenhagen - Association Station - Top 5 Games with the Best Artwork",
                    },
                    {
                        "@objectid": "472096",
                        "#text": "Episode 23: Discovering the Lacerdaverse (Vital Lacerda Games)",
                    },
                    {
                        "@objectid": "322197",
                        "#text": "Episode 24 – Catching Up, Lisboa, &amp; Downforce",
                    },
                    {
                        "@objectid": "465586",
                        "#text": "Episode 28: Top 30 Countdown, Part III (10-1)",
                    },
                    {
                        "@objectid": "196138",
                        "#text": "Episode 39 - Our Most Anticipated Games in 2017",
                    },
                    {
                        "@objectid": "262250",
                        "#text": "Episode 46: Mr. Jack, Lords of Waterdeep, Apocrypha, Lisboa, KLASK",
                    },
                    {
                        "@objectid": "430924",
                        "#text": "Episode 4: Top 5 Shelf of Shame Games",
                    },
                    {
                        "@objectid": "211990",
                        "#text": "Episode 50 - Gen Con 2017 Two-Player Preview",
                    },
                    {
                        "@objectid": "227996",
                        "#text": "Episode 66 :: Charterstone Review + Best Board Games of 2017",
                    },
                    {
                        "@objectid": "475193",
                        "#text": "Expansion Pack: Birthday Boardgame Battleground - 2022 Turbo Edition",
                    },
                    {
                        "@objectid": "227730",
                        "#text": "It’s Our Turn! Episode #45: Ancient Era Games",
                    },
                    {"@objectid": "219335", "#text": "MHGG Review - Lisboa"},
                    {
                        "@objectid": "299879",
                        "#text": "Out of the Dust Ep46 - Terraforming Mars",
                    },
                    {"@objectid": "228920", "#text": "Review Episode 07 - Lisboa"},
                    {
                        "@objectid": "193133",
                        "#text": "The Dice Men Cometh – Episode 143",
                    },
                    {
                        "@objectid": "213351",
                        "#text": 'The Good The Board and The Playstyle?: Episode 129 "Playstyle"',
                    },
                    {
                        "@objectid": "211565",
                        "#text": "Vox Republica 148: Combating The Pile of Shame",
                    },
                    {
                        "@objectid": "220708",
                        "#text": "Vox Republica 155: Charitable Gaming",
                    },
                    {
                        "@objectid": "157900",
                        "#text": "What Did You Play This Week Podcast Thing Week 37!!!",
                    },
                    {
                        "@objectid": "220091",
                        "#text": "Winning The One’s Affection – Ep. 1",
                    },
                ],
                "boardgameversion": [
                    {"@objectid": "627704", "#text": "Chinese edition"},
                    {
                        "@objectid": "642938",
                        "#text": "Czech/English Deluxe Kickstarter edition",
                    },
                    {"@objectid": "395932", "#text": "English deluxe edition"},
                    {"@objectid": "244339", "#text": "English standard edition"},
                    {"@objectid": "595357", "#text": "French deluxe edition"},
                    {"@objectid": "456758", "#text": "German deluxe edition"},
                    {"@objectid": "612861", "#text": "Hungarian edition"},
                    {"@objectid": "370519", "#text": "Italian edition"},
                    {"@objectid": "498827", "#text": "Korean edition"},
                    {"@objectid": "361341", "#text": "Polish edition"},
                    {"@objectid": "372724", "#text": "Portuguese edition"},
                    {"@objectid": "578441", "#text": "Russian deluxe edition"},
                    {"@objectid": "558265", "#text": "Spanish edition"},
                ],
                "boardgamefamily": [
                    {"@objectid": "43603", "#text": "Cities: Lisbon (Portugal)"},
                    {"@objectid": "65191", "#text": "Components: Multi-Use Cards"},
                    {"@objectid": "5614", "#text": "Country: Portugal"},
                    {"@objectid": "25292", "#text": "Crowdfunding: Giochistarter"},
                    {"@objectid": "8374", "#text": "Crowdfunding: Kickstarter"},
                    {"@objectid": "22135", "#text": "Crowdfunding: Spieleschmiede"},
                    {
                        "@objectid": "70948",
                        "#text": "Digital Implementations: Tabletopia",
                    },
                    {"@objectid": "78680", "#text": "Misc: Made by Panda"},
                    {
                        "@objectid": "5666",
                        "#text": "Players: Games with Solitaire Rules",
                    },
                    {"@objectid": "73380", "#text": "Theme: Earthquakes"},
                ],
                "boardgamecategory": [
                    {"@objectid": "1029", "#text": "City Building"},
                    {"@objectid": "1021", "#text": "Economic"},
                    {"@objectid": "1088", "#text": "Industry / Manufacturing"},
                    {"@objectid": "1001", "#text": "Political"},
                ],
                "boardgamedeveloper": [
                    {"@objectid": "56863", "#text": "Paul Incao"},
                    {"@objectid": "112575", "#text": "Julián Pombo"},
                ],
                "boardgamedesigner": {"@objectid": "12396", "#text": "Vital Lacerda"},
                "boardgamesolodesigner": [
                    {"@objectid": "12396", "#text": "Vital Lacerda"},
                    {"@objectid": "112575", "#text": "Julián Pombo"},
                ],
                "boardgameaccessory": [
                    {"@objectid": "232915", "#text": "Lisboa: Heavy Cardboard Promo"},
                    {"@objectid": "237375", "#text": "Lisboa: Metal Coins"},
                    {"@objectid": "290603", "#text": "Lisboa: Upgrade Pack"},
                ],
                "boardgameexpansion": {
                    "@objectid": "301771",
                    "#text": "Lisboa: Queen Variant",
                },
                "boardgameimplementation": {
                    "@objectid": "262477",
                    "#text": "Mercado de Lisboa",
                },
                "boardgameartist": {"@objectid": "64844", "#text": "Ian O'Toole"},
                "boardgamegraphicdesigner": {
                    "@objectid": "64844",
                    "#text": "Ian O'Toole",
                },
                "boardgamesubdomain": {"@objectid": "5497", "#text": "Strategy Games"},
                "poll": [
                    {
                        "@name": "suggested_numplayers",
                        "@title": "User Suggested Number of Players",
                        "@totalvotes": "259",
                        "results": [
                            {
                                "@numplayers": "1",
                                "result": [
                                    {"@value": "Best", "@numvotes": "5"},
                                    {"@value": "Recommended", "@numvotes": "88"},
                                    {"@value": "Not Recommended", "@numvotes": "44"},
                                ],
                            },
                            {
                                "@numplayers": "2",
                                "result": [
                                    {"@value": "Best", "@numvotes": "44"},
                                    {"@value": "Recommended", "@numvotes": "139"},
                                    {"@value": "Not Recommended", "@numvotes": "20"},
                                ],
                            },
                            {
                                "@numplayers": "3",
                                "result": [
                                    {"@value": "Best", "@numvotes": "154"},
                                    {"@value": "Recommended", "@numvotes": "50"},
                                    {"@value": "Not Recommended", "@numvotes": "2"},
                                ],
                            },
                            {
                                "@numplayers": "4",
                                "result": [
                                    {"@value": "Best", "@numvotes": "48"},
                                    {"@value": "Recommended", "@numvotes": "115"},
                                    {"@value": "Not Recommended", "@numvotes": "30"},
                                ],
                            },
                            {
                                "@numplayers": "4+",
                                "result": [
                                    {"@value": "Best", "@numvotes": "0"},
                                    {"@value": "Recommended", "@numvotes": "0"},
                                    {"@value": "Not Recommended", "@numvotes": "85"},
                                ],
                            },
                        ],
                    },
                    {
                        "@name": "language_dependence",
                        "@title": "Language Dependence",
                        "@totalvotes": "14",
                        "results": {
                            "result": [
                                {
                                    "@level": "6",
                                    "@value": "No necessary in-game text",
                                    "@numvotes": "10",
                                },
                                {
                                    "@level": "7",
                                    "@value": "Some necessary text - easily memorized or small crib sheet",
                                    "@numvotes": "4",
                                },
                                {
                                    "@level": "8",
                                    "@value": "Moderate in-game text - needs crib sheet or paste ups",
                                    "@numvotes": "0",
                                },
                                {
                                    "@level": "9",
                                    "@value": "Extensive use of text - massive conversion needed to be playable",
                                    "@numvotes": "0",
                                },
                                {
                                    "@level": "10",
                                    "@value": "Unplayable in another language",
                                    "@numvotes": "0",
                                },
                            ]
                        },
                    },
                    {
                        "@name": "suggested_playerage",
                        "@title": "User Suggested Player Age",
                        "@totalvotes": "42",
                        "results": {
                            "result": [
                                {"@value": "2", "@numvotes": "0"},
                                {"@value": "3", "@numvotes": "0"},
                                {"@value": "4", "@numvotes": "0"},
                                {"@value": "5", "@numvotes": "0"},
                                {"@value": "6", "@numvotes": "0"},
                                {"@value": "8", "@numvotes": "0"},
                                {"@value": "10", "@numvotes": "1"},
                                {"@value": "12", "@numvotes": "8"},
                                {"@value": "14", "@numvotes": "19"},
                                {"@value": "16", "@numvotes": "12"},
                                {"@value": "18", "@numvotes": "2"},
                                {"@value": "21 and up", "@numvotes": "0"},
                            ]
                        },
                    },
                ],
            },
            {
                "@objectid": "164153",
                "yearpublished": "2014",
                "minplayers": "1",
                "maxplayers": "5",
                "playingtime": "120",
                "minplaytime": "60",
                "maxplaytime": "120",
                "age": "14",
                "name": [
                    {"@sortindex": "1", "#text": "Star Wars: Assalto Imperiale"},
                    {"@sortindex": "1", "#text": "Star Wars: Assaut sur l'Empire"},
                    {
                        "@primary": "true",
                        "@sortindex": "1",
                        "#text": "Star Wars: Imperial Assault",
                    },
                    {"@sortindex": "1", "#text": "Star Wars: Imperium Atakuje"},
                    {"@sortindex": "1", "#text": "星際大戰：帝國突襲"},
                ],
                "description": "This page does not exist. You can edit this page to create it.",
                "thumbnail": "https://cf.geekdo-images.com/pIQ_MXvaoARRp1loCHJuHg__thumb/img/AD5YvNSUaVvITmtQb1-b01VuBbs=/fit-in/200x150/filters:strip_icc()/pic2247647.jpg",
                "image": "https://cf.geekdo-images.com/pIQ_MXvaoARRp1loCHJuHg__original/img/12Xvbw01hpsAjsO0xrajZt2b5HY=/0x0/filters:format(jpeg)/pic2247647.jpg",
                "boardgamepublisher": [
                    {"@objectid": "17", "#text": "Fantasy Flight Games"},
                    {"@objectid": "15889", "#text": "Asterion Press"},
                    {"@objectid": "2973", "#text": "Edge Entertainment"},
                    {"@objectid": "4617", "#text": "Galakta"},
                    {"@objectid": "15605", "#text": "Galápagos Jogos"},
                    {"@objectid": "264", "#text": "Heidelberger Spieleverlag"},
                    {"@objectid": "18852", "#text": "Hobby World"},
                ],
                "boardgamepodcastepisode": [
                    {"@objectid": "223369", "#text": "#3: Hansa Teutonica and Theme"},
                    {
                        "@objectid": "152506",
                        "#text": "#80 – Tabletop – Fantasy Flight Star Wars Games",
                    },
                    {
                        "@objectid": "228001",
                        "#text": "#9: Sidereal Confluence and HATE",
                    },
                    {"@objectid": "182953", "#text": "1P 103 - Burgle Bros."},
                    {"@objectid": "296934", "#text": "6-25-19"},
                    {
                        "@objectid": "163427",
                        "#text": "7LandHand: Episode 51 – Imperial Assault",
                    },
                    {
                        "@objectid": "177525",
                        "#text": "BGA Episode 100 - Top 100 Games of All Time",
                    },
                    {"@objectid": "325098", "#text": "Black Friday Bonus Episode"},
                    {
                        "@objectid": "140443",
                        "#text": "Boardcast News 4.3.2015 | Podcast of Nonsensical Gamers",
                    },
                    {
                        "@objectid": "180825",
                        "#text": "Cult of the New Board Game Podcast Episode 018 – Star Wars: Rebellion vs Star Wars: Imperial Assault",
                    },
                    {
                        "@objectid": "137637",
                        "#text": "Dukes of Dice - Ep. 28 - Between Two Droids",
                    },
                    {
                        "@objectid": "171288",
                        "#text": "Ep 022 – Ringing in 2016 with Board Gaming!",
                    },
                    {
                        "@objectid": "252168",
                        "#text": "Ep 070 &ndash; 3rd Anniversary Special &amp; Tournament to the Death!!!",
                    },
                    {"@objectid": "169628", "#text": "Ep 33 STAR WARS with Alex Eding"},
                    {
                        "@objectid": "188652",
                        "#text": "Episode 1 - Blood Rage vs Champions of Midgard",
                    },
                    {
                        "@objectid": "143018",
                        "#text": "Episode 1 - Our Introduction Into Gaming",
                    },
                    {
                        "@objectid": "200200",
                        "#text": "Episode 10 - 7 Wonders vs Among the Stars",
                    },
                    {
                        "@objectid": "189057",
                        "#text": "Episode 10 - Space: The Final Frontier",
                    },
                    {
                        "@objectid": "298162",
                        "#text": "Episode 106 :: Best Boardgames - Brawling Brothers Blend 2019",
                    },
                    {"@objectid": "203860", "#text": "Episode 11 - Notre Dame vs Ulm"},
                    {
                        "@objectid": "196208",
                        "#text": "Episode 11: The one about our 10x10 Challenge",
                    },
                    {
                        "@objectid": "205449",
                        "#text": "Episode 12 - Tammany Hall vs Rialto",
                    },
                    {
                        "@objectid": "206562",
                        "#text": "Episode 13 - the first Dungeons and Dragons episode",
                    },
                    {
                        "@objectid": "315342",
                        "#text": "Episode 13 - The Imperial Campaign",
                    },
                    {
                        "@objectid": "233977",
                        "#text": "Episode 13 - We Are Super Hip! (Twilight Imperium IV, Clans of Caledonia, Charterstone, and more!)",
                    },
                    {
                        "@objectid": "209050",
                        "#text": "Episode 14 - Tragedy Looper vs T.I.M.E. Stories",
                    },
                    {"@objectid": "391320", "#text": "Episode 145 :: Joy of the Stick"},
                    {
                        "@objectid": "211290",
                        "#text": "Episode 15 - Roll for the Galaxy vs Tiny Epic Galaxies",
                    },
                    {
                        "@objectid": "214156",
                        "#text": "Episode 16 - Dungeon Run vs Masmorra: Dungeons of Arcadia",
                    },
                    {
                        "@objectid": "219237",
                        "#text": "Episode 17 - Castles of Burgundy vs Ora et Labora",
                    },
                    {
                        "@objectid": "171213",
                        "#text": "Episode 18: Codenames Review - Games of the Year - Giveaways",
                    },
                    {
                        "@objectid": "222072",
                        "#text": "Episode 19 - Vinhos vs Viticulture",
                    },
                    {
                        "@objectid": "189925",
                        "#text": "Episode 2 - Quarriors vs Dice Masters",
                    },
                    {
                        "@objectid": "162290",
                        "#text": "Episode 2 - Star Wars Special And Imperial Assault Review",
                    },
                    {"@objectid": "259436", "#text": "Episode 3 - Batteries Included"},
                    {"@objectid": "185171", "#text": "Episode 3 - Scare Tactics"},
                    {
                        "@objectid": "190625",
                        "#text": "Episode 3 - Witch of Salem vs Elder Sign - Gates of Arkham",
                    },
                    {
                        "@objectid": "207549",
                        "#text": "Episode 31 - Jonathan Ying, former FFG in-house designer",
                    },
                    {
                        "@objectid": "385553",
                        "#text": "Episode 31B - Good Tie-In Games, Part2",
                    },
                    {
                        "@objectid": "162178",
                        "#text": "Episode 35 - Interview with Greater Than Games Christopher Badell",
                    },
                    {
                        "@objectid": "191432",
                        "#text": "Episode 4 - Fury of Dracula vs Letters from Whitechapel",
                    },
                    {
                        "@objectid": "179528",
                        "#text": "Episode 49 - Star Wars: Rebellion Two Year Anniversary",
                    },
                    {
                        "@objectid": "134652",
                        "#text": "Episode 4: Star Wars: Imperial Assault, Neuroshima Hex Contest, Castles of Mad King Ludwig and Medieval Night",
                    },
                    {
                        "@objectid": "430924",
                        "#text": "Episode 4: Top 5 Shelf of Shame Games",
                    },
                    {
                        "@objectid": "192443",
                        "#text": "Episode 5 - Sentinels of the Multiverse vs Legendary: A Marvel Deck Building Game",
                    },
                    {
                        "@objectid": "135523",
                        "#text": "Episode 56: Assaulting Settlers?",
                    },
                    {
                        "@objectid": "135340",
                        "#text": "Episode 5: Kemble’s Cascade, But Wait, There’s More! and Chalk Digital",
                    },
                    {
                        "@objectid": "135996",
                        "#text": "Episode 5: Mice &amp; Mystics, Escape from New York, and Lords of Waterdeep",
                    },
                    {
                        "@objectid": "194588",
                        "#text": "Episode 6 - Stone Age vs Tzolk'in The Mayan Calendar",
                    },
                    {
                        "@objectid": "169877",
                        "#text": "Episode 63- Imperial Assault &amp; Alternate Holiday Buying Guide",
                    },
                    {
                        "@objectid": "225368",
                        "#text": "Episode 64 :: Escape Room Games Review - Questions with Cat",
                    },
                    {
                        "@objectid": "196478",
                        "#text": "Episode 7 - Glen More vs Lunarchitects",
                    },
                    {
                        "@objectid": "198218",
                        "#text": "Episode 8 - Shadows over Camelot vs Battlestar Galactica",
                    },
                    {"@objectid": "222705", "#text": "Episode 87 - Coldwater Crown"},
                    {
                        "@objectid": "223651",
                        "#text": "Episode 88 - Legacy of Dragonholt BA Holiday Special",
                    },
                    {
                        "@objectid": "170181",
                        "#text": "Episode 9 - Craig Cillessen &amp; Clockwork Wars Review",
                    },
                    {
                        "@objectid": "198659",
                        "#text": "Episode 9 - Imperial Assault Calgary Regionals",
                    },
                    {
                        "@objectid": "147474",
                        "#text": "Episode 9: Panamax, They Live, and Solforge",
                    },
                    {
                        "@objectid": "475193",
                        "#text": "Expansion Pack: Birthday Boardgame Battleground - 2022 Turbo Edition",
                    },
                    {"@objectid": "305864", "#text": "Explore It!"},
                    {"@objectid": "170060", "#text": "Favorite Games of 2015"},
                    {
                        "@objectid": "200187",
                        "#text": "HLG 18: Kris Burm &amp; Vooruitblik 2017",
                    },
                    {
                        "@objectid": "136168",
                        "#text": "I've Been Diced! episode 62: Our 2014 in review",
                    },
                    {
                        "@objectid": "172717",
                        "#text": "I've Been Diced! episode 71: Mutants, game studies, and 2015 in review",
                    },
                    {
                        "@objectid": "296556",
                        "#text": "Journeys In Middle-Earth, House Rules, and the Human Element in App-Based Games",
                    },
                    {
                        "@objectid": "162592",
                        "#text": "Low Player Count - Ep 13 - Luck in Games",
                    },
                    {
                        "@objectid": "140492",
                        "#text": "Low Player Count - Ep. 1 - Getting to Know You",
                    },
                    {
                        "@objectid": "174498",
                        "#text": "Low Player Count - Ep. 21 - Our Top 5 Two Player Games",
                    },
                    {
                        "@objectid": "142633",
                        "#text": "Low Player Count - Ep. 3 - High Score vs. Objective - FIGHT!",
                    },
                    {"@objectid": "164485", "#text": "Mechanics in a Name"},
                    {"@objectid": "143889", "#text": "MN 0055 Star Wars Gaming"},
                    {
                        "@objectid": "150977",
                        "#text": "MN 0061 Star Wars Imperial Assault",
                    },
                    {
                        "@objectid": "153404",
                        "#text": "MN 0065 Looking Back and Looking Forward",
                    },
                    {
                        "@objectid": "140504",
                        "#text": "MOBG podcast 29 Super Motherload 01-04-15",
                    },
                    {
                        "@objectid": "291740",
                        "#text": "Out of the Dust Ep40 - Walnut Grove",
                    },
                    {"@objectid": "138292", "#text": "Podcast #1 – Humble Beginnings"},
                    {
                        "@objectid": "155722",
                        "#text": "Podcast #10 – Singing Heroes of GENCON",
                    },
                    {"@objectid": "158090", "#text": "Podcast #11 – Hot and Cold"},
                    {
                        "@objectid": "160451",
                        "#text": "Podcast #12 – Jar Jar Binks is a Fool",
                    },
                    {
                        "@objectid": "162078",
                        "#text": "Podcast #13 – Kobayashi A new Threat",
                    },
                    {"@objectid": "162778", "#text": "Podcast #14 – Only 50 Euro"},
                    {"@objectid": "163692", "#text": "Podcast #15 – Weakened"},
                    {
                        "@objectid": "164509",
                        "#text": "Podcast #16 – Scrambled Communication",
                    },
                    {"@objectid": "165900", "#text": "Podcast #17 – Into the Cold"},
                    {"@objectid": "168554", "#text": "Podcast #18 – Herwig Hawking"},
                    {
                        "@objectid": "169639",
                        "#text": "Podcast #19 – Maurading Mercenary",
                    },
                    {
                        "@objectid": "139135",
                        "#text": "Podcast #2 – Flying out of the Box",
                    },
                    {"@objectid": "172301", "#text": "Podcast #20 – Miracle Host"},
                    {"@objectid": "174323", "#text": "Podcast #21 – Gideon MVP"},
                    {"@objectid": "174994", "#text": "Podcast #22 – Learn on the Fly"},
                    {
                        "@objectid": "176160",
                        "#text": "Podcast #23 – Boring but Efficient",
                    },
                    {
                        "@objectid": "177132",
                        "#text": "Podcast #24 – Sauerkraut Icecreme",
                    },
                    {"@objectid": "177800", "#text": "Podcast #25 – Bitchy But Good"},
                    {"@objectid": "178969", "#text": "Podcast #26 – Monkey Recording"},
                    {"@objectid": "179823", "#text": "Podcast #27 – Painting Troll"},
                    {
                        "@objectid": "181631",
                        "#text": "Podcast #28 – Gideon and Murne equals Gurne",
                    },
                    {"@objectid": "183190", "#text": "Podcast #29 – Time Machine"},
                    {"@objectid": "140541", "#text": "Podcast #3 – Therapy Session"},
                    {"@objectid": "184122", "#text": "Podcast #30 – Sidemouthed"},
                    {
                        "@objectid": "184522",
                        "#text": "Podcast #31 – Stealing Hearts and Cards",
                    },
                    {
                        "@objectid": "185515",
                        "#text": "Podcast #32 – The new Hoth thing to do",
                    },
                    {"@objectid": "186523", "#text": "Podcast #33 – NOT Gencon"},
                    {"@objectid": "188249", "#text": "Podcast #34 – Jabba Jetpack"},
                    {
                        "@objectid": "189373",
                        "#text": "Podcast #35 – Aqualish Bowling Ball",
                    },
                    {"@objectid": "190797", "#text": "Podcast #36 – Trade Fair Fever"},
                    {"@objectid": "192032", "#text": "Podcast #37 – Whining Farmboy"},
                    {
                        "@objectid": "193468",
                        "#text": "Podcast #38 – Flame Resistant Dewback",
                    },
                    {
                        "@objectid": "195113",
                        "#text": "Podcast #39 – Allegations of a Cold",
                    },
                    {"@objectid": "142033", "#text": "Podcast #4 – Combat Slug"},
                    {"@objectid": "195753", "#text": "Podcast #40 – Aqualish for 2"},
                    {"@objectid": "196882", "#text": "Podcast #41 – The Pasi Rule"},
                    {
                        "@objectid": "199009",
                        "#text": "Podcast #42 – The Answer To Life And Possibly Skirmish",
                    },
                    {"@objectid": "199583", "#text": "Podcast #43 – Wookie Hate"},
                    {"@objectid": "204591", "#text": "Podcast #44 – Coughing Contest"},
                    {"@objectid": "206253", "#text": "Podcast #46 – Full of Crumbs"},
                    {"@objectid": "207677", "#text": "Podcast #47 – Use the Swartz"},
                    {"@objectid": "208861", "#text": "Podcast #48 – Hot in the City"},
                    {"@objectid": "210515", "#text": "Podcast #49 – Ghetto Solution"},
                    {"@objectid": "143143", "#text": "Podcast #5 – Wookie Throw"},
                    {"@objectid": "213601", "#text": "Podcast #50 – Happy Birthday"},
                    {"@objectid": "214323", "#text": "Podcast #51 – Sauna Party"},
                    {"@objectid": "218704", "#text": "Podcast #52 – Edgy Case"},
                    {"@objectid": "219341", "#text": "Podcast #53 – HotE the Door"},
                    {"@objectid": "220399", "#text": "Podcast #54 – Giving Advice"},
                    {"@objectid": "222478", "#text": "Podcast #55 – She is a SNAIL"},
                    {
                        "@objectid": "224177",
                        "#text": "Podcast #56 – Whole LotA Playing",
                    },
                    {
                        "@objectid": "224970",
                        "#text": "Podcast #57 – Coming Back Around",
                    },
                    {"@objectid": "227864", "#text": "Podcast #58 – Carrier Pigeon"},
                    {"@objectid": "145672", "#text": "Podcast #6 – Ewok Army"},
                    {"@objectid": "150000", "#text": "Podcast #7 – High Explosives"},
                    {"@objectid": "152511", "#text": "Podcast #8 – Breaking the Mold"},
                    {"@objectid": "153494", "#text": "Podcast #9 – Generic Smuggler"},
                    {"@objectid": "192645", "#text": "Podcast – Worlds 2016 Special"},
                    {
                        "@objectid": "160562",
                        "#text": "RJ51: Jocs de taula i política amb Jason Matthews",
                    },
                    {
                        "@objectid": "187879",
                        "#text": "Se Viene La Lluvia 03x04 - Especial Tematico: Star Wars",
                    },
                    {
                        "@objectid": "187353",
                        "#text": "Special Podcast – Interview with Paul and Todd of FFG",
                    },
                    {"@objectid": "180983", "#text": "Star Wars special"},
                    {"@objectid": "228000", "#text": "TGT 075: Table Flippers"},
                    {
                        "@objectid": "136601",
                        "#text": "The Game Pit: Episode 40 - Council Chamber Mega Review of 2014 with Top 5s",
                    },
                    {
                        "@objectid": "143327",
                        "#text": "The Game Pit: Episode 44 - Lobstercon",
                    },
                    {
                        "@objectid": "164282",
                        "#text": "The Good, The Board and The Fluffy:  Episode 43 “Jonathan’s Top Ten”",
                    },
                    {
                        "@objectid": "163949",
                        "#text": "The Good, The Board and The Guru:  Episode 42 “Trent’s Top 10″",
                    },
                    {
                        "@objectid": "251172",
                        "#text": "Top 50 Games of All Time - 50 to 41",
                    },
                    {
                        "@objectid": "139641",
                        "#text": "Total Con 2015: Stalking Frank Mentzer",
                    },
                    {
                        "@objectid": "164589",
                        "#text": "What Did You Play This Week Podcast Thing Week 49!! Featuring Chris and Joe from Cardboard Architects, Eric Booth, AnnaBeth and Kerensa",
                    },
                    {
                        "@objectid": "168787",
                        "#text": "What Did You Play This Week Podcast Thing Week 54!!!!",
                    },
                ],
                "boardgamehonor": [
                    {
                        "@objectid": "61408",
                        "#text": "2014 Board Game Quest Awards Best Production Values Nominee",
                    },
                    {
                        "@objectid": "61406",
                        "#text": "2014 Board Game Quest Awards Best Tactical/Combat Game Nominee",
                    },
                    {
                        "@objectid": "61420",
                        "#text": "2014 Board Game Quest Awards Best Tactical/Combat Game Winner",
                    },
                    {
                        "@objectid": "61405",
                        "#text": "2014 Board Game Quest Awards Best Thematic Game Nominee",
                    },
                    {
                        "@objectid": "61404",
                        "#text": "2014 Board Game Quest Awards Game of the Year Nominee",
                    },
                    {
                        "@objectid": "26776",
                        "#text": "2014 Golden Geek Best Board Game Artwork & Presentation Nominee",
                    },
                    {
                        "@objectid": "26788",
                        "#text": "2014 Golden Geek Best Thematic Board Game Nominee",
                    },
                    {
                        "@objectid": "26773",
                        "#text": "2014 Golden Geek Board Game of the Year Nominee",
                    },
                    {"@objectid": "27655", "#text": "2014 Meeples' Choice Nominee"},
                    {"@objectid": "65398", "#text": "2015 Juego del Año Recommended"},
                    {"@objectid": "35457", "#text": "2015 Tric Trac Nominee"},
                    {
                        "@objectid": "41184",
                        "#text": "2015 UK Games Expo Best Boardgame with Miniatures Winner",
                    },
                    {"@objectid": "34820", "#text": "2016 Goblin Magnifico Nominee"},
                ],
                "boardgamecategory": [
                    {"@objectid": "1022", "#text": "Adventure"},
                    {"@objectid": "1020", "#text": "Exploration"},
                    {"@objectid": "1046", "#text": "Fighting"},
                    {"@objectid": "1047", "#text": "Miniatures"},
                    {"@objectid": "1064", "#text": "Movies / TV / Radio theme"},
                    {"@objectid": "1016", "#text": "Science Fiction"},
                    {"@objectid": "1019", "#text": "Wargame"},
                ],
                "boardgamedeveloper": [
                    {"@objectid": "71982", "#text": "Samuel Bailey"},
                    {"@objectid": "111355", "#text": "Jason Walden"},
                ],
                "boardgameartist": [
                    {"@objectid": "78030", "#text": "Arden Beckwith"},
                    {"@objectid": "19411", "#text": "Christopher Burdett"},
                    {"@objectid": "72509", "#text": "Rovina Cai"},
                    {"@objectid": "73895", "#text": "Lucas Durham"},
                    {"@objectid": "69246", "#text": "Joel Hustak"},
                    {"@objectid": "36621", "#text": "Michal Ivan"},
                    {"@objectid": "48500", "#text": "David Kegg"},
                    {"@objectid": "24858", "#text": "Henning Ludvigsen"},
                    {"@objectid": "47549", "#text": "Brynn Metheney"},
                    {"@objectid": "104761", "#text": "Vlad Ricean"},
                    {"@objectid": "68942", "#text": "Ryan Valle"},
                    {"@objectid": "49280", "#text": "Ben Zweifel"},
                ],
                "boardgamefamily": [
                    {"@objectid": "59218", "#text": "Category: Dungeon Crawler"},
                    {"@objectid": "65328", "#text": "Components: Dice with Icons"},
                    {"@objectid": "25158", "#text": "Components: Miniatures"},
                    {"@objectid": "26488", "#text": "Game: Star Wars Imperial Assault"},
                    {"@objectid": "24281", "#text": "Mechanism: Campaign Games"},
                    {"@objectid": "5602", "#text": "Movies: Star Wars"},
                    {
                        "@objectid": "5666",
                        "#text": "Players: Games with Solitaire Rules",
                    },
                    {"@objectid": "49383", "#text": "Players: One versus Many"},
                ],
                "boardgameversion": [
                    {"@objectid": "385067", "#text": "Chinese edition"},
                    {"@objectid": "248956", "#text": "English edition"},
                    {"@objectid": "263058", "#text": "French edition"},
                    {"@objectid": "254037", "#text": "German edition"},
                    {"@objectid": "275395", "#text": "Italian edition"},
                    {"@objectid": "261912", "#text": "Polish edition"},
                    {"@objectid": "322162", "#text": "Portuguese edition"},
                    {"@objectid": "408004", "#text": "Russian edition"},
                    {"@objectid": "257777", "#text": "Spanish edition"},
                ],
                "boardgamemechanic": [
                    {"@objectid": "2072", "#text": "Dice Rolling"},
                    {"@objectid": "2856", "#text": "Die Icon Resolution"},
                    {"@objectid": "2676", "#text": "Grid Movement"},
                    {"@objectid": "2975", "#text": "Line of Sight"},
                    {"@objectid": "2011", "#text": "Modular Board"},
                    {"@objectid": "2028", "#text": "Role Playing"},
                    {
                        "@objectid": "2822",
                        "#text": "Scenario / Mission / Campaign Game",
                    },
                    {"@objectid": "2940", "#text": "Square Grid"},
                    {"@objectid": "2019", "#text": "Team-Based Game"},
                    {"@objectid": "2015", "#text": "Variable Player Powers"},
                ],
                "commerceweblink": {
                    "@objectid": "301434",
                    "#text": "Geek Game Shop listing for Star Wars Imperial Assault",
                },
                "boardgamedesigner": [
                    {"@objectid": "72460", "#text": "Justin Kemppainen"},
                    {"@objectid": "6651", "#text": "Corey Konieczka"},
                    {"@objectid": "78796", "#text": "Jonathan Ying"},
                ],
                "boardgamegraphicdesigner": {
                    "@objectid": "12436",
                    "#text": "WiL Springer",
                },
                "videogamebg": {
                    "@objectid": "243494",
                    "#text": "Star Wars: Imperial Assault",
                },
                "boardgameaccessory": [
                    {
                        "@objectid": "249126",
                        "#text": "Star Wars: Imperial Assault – Agent Blaise Alternate Art",
                    },
                    {
                        "@objectid": "249127",
                        "#text": "Star Wars: Imperial Assault – Ahsoka Tano Alternate Art",
                    },
                    {
                        "@objectid": "249128",
                        "#text": "Star Wars: Imperial Assault – Alliance Smuggler Alternate Art",
                    },
                    {
                        "@objectid": "219794",
                        "#text": "Star Wars: Imperial Assault – Anchorhead Cantina Skirmish Map",
                    },
                    {
                        "@objectid": "249129",
                        "#text": "Star Wars: Imperial Assault – AT-DP Alternate Art",
                    },
                    {
                        "@objectid": "249131",
                        "#text": "Star Wars: Imperial Assault – AT-ST Alternate Art",
                    },
                    {
                        "@objectid": "249228",
                        "#text": "Star Wars: Imperial Assault – Bantha Rider Alternate Art",
                    },
                    {
                        "@objectid": "249230",
                        "#text": "Star Wars: Imperial Assault – Boba Fett Alternate Art",
                    },
                    {
                        "@objectid": "249231",
                        "#text": "Star Wars: Imperial Assault – Bossk Alternate Art",
                    },
                    {
                        "@objectid": "250128",
                        "#text": "Star Wars: Imperial Assault – C-3PO Alternate Art",
                    },
                    {
                        "@objectid": "259259",
                        "#text": "Star Wars: Imperial Assault – Captain Terro Alternate Art",
                    },
                    {
                        "@objectid": "250129",
                        "#text": "Star Wars: Imperial Assault – Chewbacca Alternate Art",
                    },
                    {
                        "@objectid": "250130",
                        "#text": "Star Wars: Imperial Assault – Darth Vader Alternate Art",
                    },
                    {
                        "@objectid": "250131",
                        "#text": "Star Wars: Imperial Assault – Dengar Alternate Art",
                    },
                    {
                        "@objectid": "259256",
                        "#text": "Star Wars: Imperial Assault – Dewback Rider Alternate Art",
                    },
                    {
                        "@objectid": "250132",
                        "#text": "Star Wars: Imperial Assault – Diala Passil Alternate Art",
                    },
                    {
                        "@objectid": "167706",
                        "#text": "Star Wars: Imperial Assault – Dice Pack",
                    },
                    {
                        "@objectid": "259266",
                        "#text": "Star Wars: Imperial Assault – Driven by Hatred Alternate Art",
                    },
                    {
                        "@objectid": "309480",
                        "#text": "Star Wars: Imperial Assault – e-Raptor Insert",
                    },
                    {
                        "@objectid": "259268",
                        "#text": "Star Wars: Imperial Assault – E-web Engineer Alternate Art",
                    },
                    {
                        "@objectid": "259272",
                        "#text": "Star Wars: Imperial Assault – Emperor Palpatine Alternate Art",
                    },
                    {
                        "@objectid": "259311",
                        "#text": "Star Wars: Imperial Assault – Fenn Signis Alternate Art",
                    },
                    {
                        "@objectid": "297891",
                        "#text": "Star Wars: Imperial Assault – Gaarkhan (Hero) Alternate Art",
                    },
                    {
                        "@objectid": "297890",
                        "#text": "Star Wars: Imperial Assault – Gaarkhan Alternate Art",
                    },
                    {
                        "@objectid": "259315",
                        "#text": "Star Wars: Imperial Assault – General Weiss Alternate Art",
                    },
                    {
                        "@objectid": "304296",
                        "#text": "Star Wars: Imperial Assault – Gray Cap Cantina Raid Map",
                    },
                    {
                        "@objectid": "259316",
                        "#text": "Star Wars: Imperial Assault – Han Solo Alternate Art",
                    },
                    {
                        "@objectid": "259318",
                        "#text": "Star Wars: Imperial Assault – Hera Syndula Alternate Art",
                    },
                    {
                        "@objectid": "259320",
                        "#text": "Star Wars: Imperial Assault – Heroic Effort Alternate Art",
                    },
                    {
                        "@objectid": "259321",
                        "#text": "Star Wars: Imperial Assault – HK Assassin Droid Alternate Art",
                    },
                    {
                        "@objectid": "259324",
                        "#text": "Star Wars: Imperial Assault – IG-88 Alternate Art",
                    },
                    {
                        "@objectid": "259325",
                        "#text": "Star Wars: Imperial Assault – Imperial Officer Alternate Art",
                    },
                    {
                        "@objectid": "271317",
                        "#text": "Star Wars: Imperial Assault – Imperial Organizer",
                    },
                    {
                        "@objectid": "274303",
                        "#text": "Star Wars: Imperial Assault – Imperial Organizer – Extra Dividers",
                    },
                    {
                        "@objectid": "213719",
                        "#text": "Star Wars: Imperial Assault – ISB Headquarters Skirmish Map",
                    },
                    {
                        "@objectid": "224427",
                        "#text": "Star Wars: Imperial Assault – Jabba's Palace Skirmish Map",
                    },
                    {
                        "@objectid": "259474",
                        "#text": "Star Wars: Imperial Assault – Jawa Scavenger Alternate Art",
                    },
                    {
                        "@objectid": "259476",
                        "#text": "Star Wars: Imperial Assault – Junk Droid Alternate Art",
                    },
                    {
                        "@objectid": "297725",
                        "#text": "Star Wars: Imperial Assault – Jyn Odan (Hero) Alternate Art",
                    },
                    {
                        "@objectid": "297727",
                        "#text": "Star Wars: Imperial Assault – Jyn Odan Alternate Art",
                    },
                    {
                        "@objectid": "259478",
                        "#text": "Star Wars: Imperial Assault – Kanan Jarrus Alternate Art",
                    },
                    {
                        "@objectid": "259479",
                        "#text": "Star Wars: Imperial Assault – Kayn Somos Alternate Art",
                    },
                    {
                        "@objectid": "259480",
                        "#text": "Star Wars: Imperial Assault – Lando Calrissian Alternate Art",
                    },
                    {
                        "@objectid": "326840",
                        "#text": "Star Wars: Imperial Assault – Laserox Imperial Insert",
                    },
                    {
                        "@objectid": "259481",
                        "#text": "Star Wars: Imperial Assault – Leia Organa Alternate Art",
                    },
                    {
                        "@objectid": "297730",
                        "#text": "Star Wars: Imperial Assault – Longblaster Alternate Art",
                    },
                    {
                        "@objectid": "255213",
                        "#text": "Star Wars: Imperial Assault – Lothal Wastes Skirmish Map",
                    },
                    {
                        "@objectid": "259482",
                        "#text": "Star Wars: Imperial Assault – Luke Skywalker Alternate Art",
                    },
                    {
                        "@objectid": "259483",
                        "#text": "Star Wars: Imperial Assault – Luke Skywalker, Jedi Knight Alternate Art",
                    },
                    {
                        "@objectid": "297731",
                        "#text": "Star Wars: Imperial Assault – Mak Eshka'rey (Hero) Alternate Art",
                    },
                    {
                        "@objectid": "297732",
                        "#text": "Star Wars: Imperial Assault – Mak Eshka'rey Alternate Art",
                    },
                    {
                        "@objectid": "282892",
                        "#text": "Star Wars: Imperial Assault – Malastarian Outpost Raid Map",
                    },
                    {
                        "@objectid": "248513",
                        "#text": "Star Wars: Imperial Assault – Mos Eisley Back Alleys Skirmish Map",
                    },
                    {
                        "@objectid": "231670",
                        "#text": "Star Wars: Imperial Assault – Nal Hutta Swamps Skirmish Map",
                    },
                    {
                        "@objectid": "259484",
                        "#text": "Star Wars: Imperial Assault – Nexu Alternate Art",
                    },
                    {
                        "@objectid": "259485",
                        "#text": "Star Wars: Imperial Assault – Obi-Wan Kenobi Alternate Art",
                    },
                    {
                        "@objectid": "259486",
                        "#text": "Star Wars: Imperial Assault – Probe Droid Alternate Art",
                    },
                    {
                        "@objectid": "259813",
                        "#text": "Star Wars: Imperial Assault – R2-D2 Alternate Art",
                    },
                    {
                        "@objectid": "259814",
                        "#text": "Star Wars: Imperial Assault – Rebel Saboteurs Alternate Art",
                    },
                    {
                        "@objectid": "259815",
                        "#text": "Star Wars: Imperial Assault – Rebel Trooper Alternate Art",
                    },
                    {
                        "@objectid": "297888",
                        "#text": "Star Wars: Imperial Assault – Royal Guard Alternate Art",
                    },
                    {
                        "@objectid": "353729",
                        "#text": "Star Wars: Imperial Assault – The Broken Token's Imperial Organizer",
                    },
                    {
                        "@objectid": "259313",
                        "#text": "Star Wars: Imperial Assault – The Grand Inquisitor Alternate Art",
                    },
                    {
                        "@objectid": "255214",
                        "#text": "Star Wars: Imperial Assault – Uscru Entertainment District Skirmish Map",
                    },
                    {
                        "@objectid": "297893",
                        "#text": "Star Wars: Imperial Assault – Vibro-Ax Alternate Art",
                    },
                    {
                        "@objectid": "297726",
                        "#text": "Star Wars: Imperial Assault – Vintage Blaster Alternate Art",
                    },
                ],
                "boardgameexpansion": [
                    {
                        "@objectid": "194901",
                        "#text": "Star Wars: Imperial Assault – Agent Blaise Villain Pack",
                    },
                    {
                        "@objectid": "226836",
                        "#text": "Star Wars: Imperial Assault – Ahsoka Tano Ally Pack",
                    },
                    {
                        "@objectid": "205902",
                        "#text": "Star Wars: Imperial Assault – Alliance Rangers Ally Pack",
                    },
                    {
                        "@objectid": "180621",
                        "#text": "Star Wars: Imperial Assault – Alliance Smuggler Ally Pack",
                    },
                    {
                        "@objectid": "180622",
                        "#text": "Star Wars: Imperial Assault – Bantha Rider Villain Pack",
                    },
                    {
                        "@objectid": "175213",
                        "#text": "Star Wars: Imperial Assault – Boba Fett Villain Pack",
                    },
                    {
                        "@objectid": "194900",
                        "#text": "Star Wars: Imperial Assault – Bossk Villain Pack",
                    },
                    {
                        "@objectid": "218254",
                        "#text": "Star Wars: Imperial Assault – BT-1 and 0-0-0 Villain Pack",
                    },
                    {
                        "@objectid": "205903",
                        "#text": "Star Wars: Imperial Assault – Captain Terro Villain Pack",
                    },
                    {
                        "@objectid": "167886",
                        "#text": "Star Wars: Imperial Assault – Chewbacca Ally Pack",
                    },
                    {
                        "@objectid": "265523",
                        "#text": "Star Wars: Imperial Assault – Coruscant Back Alleys Skirmish Map",
                    },
                    {
                        "@objectid": "299775",
                        "#text": "Star Wars: Imperial Assault – Coruscant Landfill Skirmish Map",
                    },
                    {
                        "@objectid": "181688",
                        "#text": "Star Wars: Imperial Assault – Dengar Villain Pack",
                    },
                    {
                        "@objectid": "181690",
                        "#text": "Star Wars: Imperial Assault – Echo Base Troopers Ally Pack",
                    },
                    {
                        "@objectid": "226837",
                        "#text": "Star Wars: Imperial Assault – Emperor Palpatine Villain Pack",
                    },
                    {
                        "@objectid": "278326",
                        "#text": "Star Wars: Imperial Assault – Endor Defense Station Skirmish Map",
                    },
                    {
                        "@objectid": "251227",
                        "#text": "Star Wars: Imperial Assault – Ezra Bridger and Kanan Jarrus Ally Pack",
                    },
                    {
                        "@objectid": "181629",
                        "#text": "Star Wars: Imperial Assault – General Sorin Villain Pack",
                    },
                    {
                        "@objectid": "167883",
                        "#text": "Star Wars: Imperial Assault – General Weiss Villain Pack",
                    },
                    {
                        "@objectid": "199911",
                        "#text": "Star Wars: Imperial Assault – Greedo Villain Pack",
                    },
                    {
                        "@objectid": "167889",
                        "#text": "Star Wars: Imperial Assault – Han Solo Ally Pack",
                    },
                    {
                        "@objectid": "226839",
                        "#text": "Star Wars: Imperial Assault – Heart of the Empire",
                    },
                    {
                        "@objectid": "218255",
                        "#text": "Star Wars: Imperial Assault – Hera Syndulla and C1-10P Ally Pack",
                    },
                    {
                        "@objectid": "177087",
                        "#text": "Star Wars: Imperial Assault – Hired Guns Villain Pack",
                    },
                    {
                        "@objectid": "251229",
                        "#text": "Star Wars: Imperial Assault – Hondo Ohnaka Villain Pack",
                    },
                    {
                        "@objectid": "167885",
                        "#text": "Star Wars: Imperial Assault – IG-88 Villain Pack",
                    },
                    {
                        "@objectid": "194902",
                        "#text": "Star Wars: Imperial Assault – ISB Infiltrators Villain Pack",
                    },
                    {
                        "@objectid": "205904",
                        "#text": "Star Wars: Imperial Assault – Jabba the Hutt Villain Pack",
                    },
                    {
                        "@objectid": "205900",
                        "#text": "Star Wars: Imperial Assault – Jabba's Realm",
                    },
                    {
                        "@objectid": "218253",
                        "#text": "Star Wars: Imperial Assault – Jawa Scavenger Villain Pack",
                    },
                    {
                        "@objectid": "175214",
                        "#text": "Star Wars: Imperial Assault – Kayn Somos Villain Pack",
                    },
                    {
                        "@objectid": "194903",
                        "#text": "Star Wars: Imperial Assault – Lando Calrissian Ally Pack",
                    },
                    {
                        "@objectid": "241827",
                        "#text": "Star Wars: Imperial Assault – Legends of the Alliance",
                    },
                    {
                        "@objectid": "181689",
                        "#text": "Star Wars: Imperial Assault – Leia Organa Ally Pack",
                    },
                    {
                        "@objectid": "205905",
                        "#text": "Star Wars: Imperial Assault – Luke Skywalker Jedi Knight Ally Pack",
                    },
                    {
                        "@objectid": "226838",
                        "#text": "Star Wars: Imperial Assault – Maul Villain Pack",
                    },
                    {
                        "@objectid": "299773",
                        "#text": "Star Wars: Imperial Assault – Nelvaanian War Zone Skirmish Map",
                    },
                    {
                        "@objectid": "199909",
                        "#text": "Star Wars: Imperial Assault – Obi-Wan Kenobi Ally Pack",
                    },
                    {
                        "@objectid": "175212",
                        "#text": "Star Wars: Imperial Assault – R2-D2 and C-3PO Ally Pack",
                    },
                    {
                        "@objectid": "167888",
                        "#text": "Star Wars: Imperial Assault – Rebel Saboteurs Ally Pack",
                    },
                    {
                        "@objectid": "167887",
                        "#text": "Star Wars: Imperial Assault – Rebel Troopers Ally Pack",
                    },
                    {
                        "@objectid": "181621",
                        "#text": "Star Wars: Imperial Assault – Return to Hoth",
                    },
                    {
                        "@objectid": "167884",
                        "#text": "Star Wars: Imperial Assault – Royal Guard Champion Villain Pack",
                    },
                    {
                        "@objectid": "251230",
                        "#text": "Star Wars: Imperial Assault – Sabine Wren and Zeb Orrelios Ally Pack",
                    },
                    {
                        "@objectid": "177088",
                        "#text": "Star Wars: Imperial Assault – Stormtroopers Villain Pack",
                    },
                    {
                        "@objectid": "316533",
                        "#text": "Star Wars: Imperial Assault – Tarkin Initiative Labs Skirmish Map",
                    },
                    {
                        "@objectid": "194897",
                        "#text": "Star Wars: Imperial Assault – The Bespin Gambit",
                    },
                    {
                        "@objectid": "199910",
                        "#text": "Star Wars: Imperial Assault – The Grand Inquisitor Villain Pack",
                    },
                    {
                        "@objectid": "251231",
                        "#text": "Star Wars: Imperial Assault – Thrawn Villain Pack",
                    },
                    {
                        "@objectid": "299774",
                        "#text": "Star Wars: Imperial Assault – Training Ground Skirmish Map",
                    },
                    {
                        "@objectid": "175211",
                        "#text": "Star Wars: Imperial Assault – Twin Shadows",
                    },
                    {
                        "@objectid": "251066",
                        "#text": "Star Wars: Imperial Assault – Tyrants of Lothal",
                    },
                    {
                        "@objectid": "177086",
                        "#text": "Star Wars: Imperial Assault – Wookiee Warriors Ally Pack",
                    },
                ],
                "boardgamesubdomain": {"@objectid": "5496", "#text": "Thematic Games"},
                "boardgameimplementation": [
                    {
                        "@objectid": "17226",
                        "@inbound": "true",
                        "#text": "Descent: Journeys in the Dark",
                    },
                    {
                        "@objectid": "104162",
                        "@inbound": "true",
                        "#text": "Descent: Journeys in the Dark (Second Edition)",
                    },
                ],
                "poll": [
                    {
                        "@name": "suggested_numplayers",
                        "@title": "User Suggested Number of Players",
                        "@totalvotes": "398",
                        "results": [
                            {
                                "@numplayers": "1",
                                "result": [
                                    {"@value": "Best", "@numvotes": "12"},
                                    {"@value": "Recommended", "@numvotes": "68"},
                                    {"@value": "Not Recommended", "@numvotes": "189"},
                                ],
                            },
                            {
                                "@numplayers": "2",
                                "result": [
                                    {"@value": "Best", "@numvotes": "188"},
                                    {"@value": "Recommended", "@numvotes": "120"},
                                    {"@value": "Not Recommended", "@numvotes": "25"},
                                ],
                            },
                            {
                                "@numplayers": "3",
                                "result": [
                                    {"@value": "Best", "@numvotes": "82"},
                                    {"@value": "Recommended", "@numvotes": "188"},
                                    {"@value": "Not Recommended", "@numvotes": "34"},
                                ],
                            },
                            {
                                "@numplayers": "4",
                                "result": [
                                    {"@value": "Best", "@numvotes": "59"},
                                    {"@value": "Recommended", "@numvotes": "184"},
                                    {"@value": "Not Recommended", "@numvotes": "57"},
                                ],
                            },
                            {
                                "@numplayers": "5",
                                "result": [
                                    {"@value": "Best", "@numvotes": "228"},
                                    {"@value": "Recommended", "@numvotes": "68"},
                                    {"@value": "Not Recommended", "@numvotes": "36"},
                                ],
                            },
                            {
                                "@numplayers": "5+",
                                "result": [
                                    {"@value": "Best", "@numvotes": "2"},
                                    {"@value": "Recommended", "@numvotes": "9"},
                                    {"@value": "Not Recommended", "@numvotes": "198"},
                                ],
                            },
                        ],
                    },
                    {
                        "@name": "language_dependence",
                        "@title": "Language Dependence",
                        "@totalvotes": "77",
                        "results": {
                            "result": [
                                {
                                    "@level": "11",
                                    "@value": "No necessary in-game text",
                                    "@numvotes": "0",
                                },
                                {
                                    "@level": "12",
                                    "@value": "Some necessary text - easily memorized or small crib sheet",
                                    "@numvotes": "1",
                                },
                                {
                                    "@level": "13",
                                    "@value": "Moderate in-game text - needs crib sheet or paste ups",
                                    "@numvotes": "9",
                                },
                                {
                                    "@level": "14",
                                    "@value": "Extensive use of text - massive conversion needed to be playable",
                                    "@numvotes": "56",
                                },
                                {
                                    "@level": "15",
                                    "@value": "Unplayable in another language",
                                    "@numvotes": "11",
                                },
                            ]
                        },
                    },
                    {
                        "@name": "suggested_playerage",
                        "@title": "User Suggested Player Age",
                        "@totalvotes": "118",
                        "results": {
                            "result": [
                                {"@value": "2", "@numvotes": "0"},
                                {"@value": "3", "@numvotes": "0"},
                                {"@value": "4", "@numvotes": "1"},
                                {"@value": "5", "@numvotes": "0"},
                                {"@value": "6", "@numvotes": "2"},
                                {"@value": "8", "@numvotes": "19"},
                                {"@value": "10", "@numvotes": "26"},
                                {"@value": "12", "@numvotes": "50"},
                                {"@value": "14", "@numvotes": "16"},
                                {"@value": "16", "@numvotes": "3"},
                                {"@value": "18", "@numvotes": "0"},
                                {"@value": "21 and up", "@numvotes": "1"},
                            ]
                        },
                    },
                ],
            },
        ],
    }
}
