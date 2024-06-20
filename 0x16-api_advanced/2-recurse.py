#!/usr/bin/python3
"""Recursively get the titles of all hot posts in any subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively get the titles of all hot posts in <subreddit>

    args:
        subreddit: Name of the subreddit
        hot_list: List of titiles collected so far
        after: Key of the after query according to the database
            documentation... Has to be provided as a query string
            with the endpoint url, as if it's the page number of the
            request


    return: List of all the titiles
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'test?!'}
    params = {'after': after, 'limit': 100}
    response = requests.get(url, allow_redirects=False,
                            params=params, headers=headers)

    if response.status_code != 200:
        return None

    response = response.json()
    posts = response['data']['children']
    for post in posts:
        hot_list.append(post['data']['title'])

    after = response['data']['after']
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
