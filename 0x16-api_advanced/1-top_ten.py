#!/usr/bin/python3
"""Get the top 10 posts in fur a subreddit"""
import requests


def top_ten(subreddit):
    """Get the top 10 posts in fur a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url, params={'limit': 10},
                       allow_redirects=False)
    if res.status_code != 200:
        print("None")
        return

    posts = res.json().get('data').get('children')[:10]
    for post in posts:
        print(post['data']['title'])
