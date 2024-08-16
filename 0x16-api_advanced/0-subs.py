#!/usr/bin/python3
"""
A function that queries the Reddit API and returns the number of subscribers
for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
       Return the number of subscribers given a subreddit
    """
    if isinstance(subreddit, str) = False:
        return 0
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    res = requests.get(url, headers={'User-Agent': "0x16-api_advanced:alx"},
                       allow_redirects=False)
    if res.status_code >= 200 and res.status_code < 300:
        data = res.json()['data']
        if 'subscribers' not in data:
            return 0
        return int(data['subscribers'])
    return 0
