#!/usr/bin/python3
"""Get the subscribers from a subreddit using reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Get the number of subs of <subreddit>

        args:
            subreddit: Number of subs

        return: the count or 0 incase of an error or nonexestent subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, allow_redirects=False)
    if res.status_code != 200:
        return 0

    return res.json().get("data").get("subscribers")
