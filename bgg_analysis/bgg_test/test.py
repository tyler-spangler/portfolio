"""
Tests for the bgg_analysis files
"""
import pandas as pd
import requests
from bgg_analysis.api_call import build_url, execute_api_call
from bgg_analysis.scrape_game_ids import get_game_urls, get_title_id


def test_build_url():
    """
    Tests successful run of build url function
    """
    test_df = pd.DataFrame(
        {"game_title": ["Game1", "Game2", "Game3"], "game_id": [1, 2, 3]}
    )
    actual_url = build_url(2, test_df)
    print(actual_url)
    expected_url = "https://api.geekdo.com/xmlapi/boardgame/1,2?comments=1"
    assert actual_url == expected_url
    assert isinstance(actual_url, str)


def test_execute_api_call(requests_mock):
    """
    Tests the excute api method and asserts that the return is dict
    """
    resp = """
    <boardgame objectid="161533">
    <yearpublished>2017</yearpublished>
    <minplayers>1</minplayers>
    <maxplayers>4</maxplayers>
    <playingtime>120</playingtime>
    <minplaytime>60</minplaytime>
    <maxplaytime>120</maxplaytime> 
    </boardgame>
    """
    test_url = "https://fake_api.com"
    requests_mock.get(test_url, status_code=200, text=resp)
    actual = execute_api_call(test_url)
    assert isinstance(actual, dict)


def test_api_call_failed(requests_mock):
    """
    Tests an unsuccessful api call and asserts that the return is the status code

    """
    test_url = "https://fake_api.com"
    requests_mock.get(test_url, exc=requests.exceptions.RequestException)
    actual = execute_api_call(test_url)
    assert actual is None


def test_get_title_id():
    """
    Tests successful run of building the title/id dataframe
    """
    test_list = [
        "/boardgame/ID1/name1",
        "/boardgame/ID2/name2",
        "/boardgame/ID3/name3",
    ]
    actual = get_title_id(test_list)
    expected = pd.DataFrame(
        {"game_title": ["name1", "name2", "name3"], "game_id": ["ID1", "ID2", "ID3"]}
    )
    pd.testing.assert_frame_equal(actual, expected)


def test_get_url(requests_mock):
    """
    Tests the function under successful conditions
    """
    test_url = "https://fake_url.com"
    test_text = "<a href='/boardgame/224517/brass-birmingham' class='primary'>Brass: Birmingham</a>"
    requests_mock.get(test_url, text=test_text)
    actual = get_game_urls(test_url)
    expected = {"/boardgame/224517/brass-birmingham"}
    assert actual == expected
