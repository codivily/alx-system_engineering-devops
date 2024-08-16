#!/usr/bin/python3
"""
A function that queries the Reddit API and returns the number of subscribers
for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    res = requests.get(url, headers={'User-Agent': "0x16-api_advanced:alx"}, allow_redirects=True)
    if res.status_code == requests.codes.ok:
        data = res.json()['data']
        if 'subscribers' not in data:
            return 0
        return data['subscribers']
    return 0
