import yake
import arxiv
import random


kw_extractor = yake.KeywordExtractor()
language = "en"
max_ngram_size = 3
deduplication_threshold = 0.9
numOfKeywords = 50
custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)


def get_keywords(paper_abstract):
    keywords_list = []
    keywords = custom_kw_extractor.extract_keywords(paper_abstract)
    for kw in keywords:
        key_word = kw[0]
        keywords_list.append(key_word)
    return keywords_list


def get_key_words_by_topic(topic, max_results=1000):
    topic_words_list = set()
    search = arxiv.Search(
      query=topic,
      max_results=max_results,
      sort_by=arxiv.SortCriterion.Relevance
    )
    for result in search.results():
        topic_words_list.update(get_keywords(result.summary))
    return list(topic_words_list)


def reverse_and_sort(words_list):
    reversed = []
    sorted = []
    for word in words_list:
        reversed.append(word[::-1])
    reversed.sort()
    for word in reversed:
        sorted.append(word[::-1])
    return sorted


def create_suffix_dict(topic):
    suffix_dict = dict()
    words_list = get_key_words_by_topic(topic, max_results=100)
    words_list = reverse_and_sort(words_list)
    for word in words_list:
        suffix = word[-2:]
        if suffix in suffix_dict:
            suffix_dict[suffix].append(word)
        else:
            suffix_dict.update({suffix: [word]})
    return suffix_dict


def find_rhyme(word, suffix_dict):
    word_suffix = word[-2:]
    if word_suffix in suffix_dict:
        rhymes = suffix_dict[word_suffix]
        return random.choice(rhymes)
    else:
        return word

