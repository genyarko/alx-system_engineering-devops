#!/usr/bin/python3
"""
0-subs
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, the function should return 0.

    Args:
        subreddit (str): The subreddit name to query.

    Returns:
        int: Number of subscribers or 0 if invalid subreddit.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'my-app/0.1'}  # Set a custom User-Agent

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        print("{:d}".format(number_of_subscribers(subreddit)))
