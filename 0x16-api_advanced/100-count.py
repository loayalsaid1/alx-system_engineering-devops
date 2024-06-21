#!/usr/bin/python3
"""
    Get count of given workds in all the titles of
    all the hot post in a subreddit
"""
import requests


def count_words(subreddit, word_list, counts={}, after=None):
    """
    Count the occurences for a list of words in the titiles of
    the hot posts in a sureddit collectively

    Then print them in a sortedday.. reverse count, alphabitically

    args:
        subreddit: Name of the subreddit
        word_list: List of words to get the count for
        counts: A dict to save the number of occurences per word
        after: Key of the after query according to the database
            documentation... Has to be provided as a query string
            with the endpoint url, as if it's the page number of the
            request

    return: noting
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'testing something'}
    params = {'after': after, 'limit': 100}

    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)

    if res.status_code != 200:
        return

    res = res.json()
    titles = [post['data']['title'] for post in res['data']['children']]
    for word in word_list:
        word = word.lower()
        count = sum(
            title.lower().split().count(word) for title in titles
        )
        if counts.get(word):
            counts[word] += count
        else:
            counts[word] = count

    after = res['data']['after']
    if after:
        count_words(subreddit, word_list, counts, after)
    else:
        counts = sorted(
            counts.items(), key=lambda element: (-element[1], element[0])
        )
        for keyword, count in counts:
            if count:
                print("{}: {}".format(keyword, count))
