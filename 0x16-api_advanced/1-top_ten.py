#!/usr/bin/python3
"""
A function that queries the Reddit API and
prints the first 10 hot posts listed given subreddit
"""
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json?limit=10'
    headers = {'User-Agent': '0x16-api_advanced:alx'}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == requests.codes.ok:
        data = res.json()['data']
        hot_posts = data['children']
        for post in hot_posts:
            print(post['data']['title'])
    else:
        print(None)
