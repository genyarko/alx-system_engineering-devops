#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests

def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "myBot/0.0.1"}
    params = {"limit": 100}
    if after:
        params["after"] = after
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json()
    posts = data["data"]["children"]
    for post in posts:
        hot_list.append(post["data"]["title"])
    after = data["data"]["after"]
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
