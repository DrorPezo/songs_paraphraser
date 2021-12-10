import datetime
from datetime import date
import random
import billboard
import re
from lyrics_extractor import SongLyrics


def download_lyrics(GCS_API_KEY, GCS_ENGINE_ID):
    start_date = datetime.date(2007, 1, 1)
    end_date = date.today()
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    chart = billboard.ChartData('pop-songs', date=str(random_date))
    songs = []
    for entry in chart:
        songs.append(entry.title)

    extract_lyrics = SongLyrics(GCS_API_KEY, GCS_ENGINE_ID)
    song = random.choice(songs)
    data = extract_lyrics.get_lyrics(song)
    lyrics = data['lyrics']
    lyrics = re.sub("[\(\[].*?[\)\]]", "", lyrics)
    lyrics_list = list(lyrics.split("\n"))
    lyrics_list = list(filter(('').__ne__, lyrics_list))
    return song, lyrics_list
