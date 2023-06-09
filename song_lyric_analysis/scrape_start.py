"""
Scrapes song lyrics and saves into csv file
"""
import logging
import os
import sys
from pathlib import Path
import requests
import pandas as pd
from bs4 import BeautifulSoup



logging.basicConfig(level=logging.INFO)

def project_path():
    """
    Gets the full path of the project

    """
    if 'song_lyric_analysis' in sys.argv[0]:
        return Path('song_lyric_analysis').resolve()

    return Path('portfolio')

def get_song_links(artist: str) -> list:
    """
    Pulls all of the links to the song lyrics for a given artist
    Parameters
    ------------
    artist: str
        name of the artist
    Return
    -------
    song_links: list
        List of all links to the songs of the artist
    """
    artist = artist.lower().replace(" ", "")
    url = f"https://www.azlyrics.com/{list(artist)[0]}/{artist}.html"
    page_content = requests.get(url, timeout=10)
    parsed_content = BeautifulSoup(page_content.content, 'html.parser')
    song_div = parsed_content.find_all('div', class_="listalbum-item")
    songs = [f"""https://www.azlyrics.com{str(s).split('"')[3]}""" for s in song_div]
    return songs

def save_song_links(song_list: list)-> None:
    """
    Saves the song links to a csv file
    Parameters
    ----------
    song_list: list
        List of links to the song lyrics
    Returns
    -------
    None
    """
    save_path = project_path()
    song_df = pd.DataFrame({'song_links': song_list})
    if "song_list.csv" in os.listdir(save_path):
        temp_df = pd.read_csv(f"{save_path}/song_list.csv")
        song_df = pd.concat([song_df, temp_df], axis=0)
        song_df.to_csv(f"{save_path}/song_list.csv", index=False)
    else:
        song_df.to_csv(f"{save_path}/song_list.csv", index=False)

    logging.info("Save complete")

#song_links = get_song_links('stick figure')
song_links = ['test1', 'test2', 'test3']
save_song_links(song_links)

#loop through and pull all links
#for song in song_links:
#    temp_song_html = requests.get(song)
#    song_soup = BeautifulSoup(temp_song_html.content, 'html.parser')
#    test = song_soup.find_all("div")
#    test_str = song_soup.get_text(separator='\n')
#    print(test_str.split('\n'))
#    break
#
#    #store song name (end  of the url) with the lyrics
