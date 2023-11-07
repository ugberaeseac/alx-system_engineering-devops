#!/usr/bin/python3
"""
queries the Reddit API
prints titles of first 10 hot posts
listed for a given subreddit
If not a valid subreddit, prints None
"""


import requests
from sys import argv


def top_ten(subreddit):
    """
    connect to reddit API
    prints titles of first 10 hot posts
    """
    subreddit = argv[1]
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    url = "https://api.reddit.com/r/{}/hot?limit=10".format(subreddit)

    urlRequest = requests.get(url, headers=headers, allow_redirects=False)
    if urlRequest.status_code == 200:
        response = urlRequest.json()
        for child in response['data']['children']:
            print(child['data']['title'])
    else:
        print(None)
