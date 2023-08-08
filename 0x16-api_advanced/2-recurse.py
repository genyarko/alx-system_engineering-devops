#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests

def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "myBot/0.0.1"}
    params = {"limit": 100}
    if after:
        params["after"] = after
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json()
    posts = data["data"]["children"]
    for post in posts:
        title = post["data"]["title"].lower()
        for word in word_list:
            if word.lower() in title and not any(c in word.lower() for c in ".!_"):
                if word.lower() in counts:
                    counts[word.lower()] += title.count(word.lower())
                else:
                    counts[word.lower()] = title.count(word.lower())
    if not counts:
        return
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")
    after = data["data"]["after"]
    count_words(subreddit, word_list, after, counts)
