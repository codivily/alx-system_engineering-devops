#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], params={}):
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    headers = {'User-Agent': '0x16-api_advanced:alx'}
    res = requests.get(url,
                       headers=headers, params=params, allow_redirects=False)
    if res.status_code == requests.codes.ok:
        data = res.json()['data']
        hot_posts = data['children']
        if len(hot_posts) > 0:
            hot_list += [item['data']['title'] for item in hot_posts]
            if data['after'] is not None:
                params['after'] = data['after']
                return recurse(subreddit, hot_list=hot_list, params=params)
    return hot_list
