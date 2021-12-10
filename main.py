from lyrics_downloader import download_lyrics
import nltk
from prepare_data import create_suffix_dict
from prepare_data import find_rhyme
import argparse


nltk.download('webtext')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def print_song(song):
    for line in song:
        print(line)
    print('\n')


if __name__ == '__main__':
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('--topic', action='store', type=str, required=True)
    args = my_parser.parse_args()
    # check here: https://github.com/Techcatchers/PyLyrics-Extractor
    # to renew GCS_API_KEY and GCS_ENGINE_ID
    GCS_API_KEY =
    GCS_ENGINE_ID =
    song, lyrics_list = download_lyrics(GCS_API_KEY, GCS_ENGINE_ID)
    print(song)
    print('\n')
    print_song(lyrics_list)
    topic = args.topic
    suffix_dict = create_suffix_dict(topic)
    new_song = []
    for line in lyrics_list:
        new_line = []
        tokens = nltk.pos_tag(nltk.word_tokenize(line))
        for token in tokens:
            word, word_type = token
            if word_type == "NN":
                word = find_rhyme(word, suffix_dict)
            new_line.append(word)
        new_line = ' '.join(new_line)
        new_song.append(new_line)
    print_song(new_song)







