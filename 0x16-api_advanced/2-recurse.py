#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import praw
import requests

def count_words(subreddit, word_list, reddit=None, counts=None, after=None):
    if reddit is None:
        reddit = praw.Reddit(user_agent='myBot/0.0.1')
    if counts is None:
        counts = {}
    try:
        hot_posts = reddit.subreddit(subreddit).hot(limit=None, params={'after': after})
    except praw.exceptions.NotFound:
        return
    for post in hot_posts:
        words = post.title.lower().split()
        for word in word_list:
            if word.lower() in words:
                if word.lower() in counts:
                    counts[word.lower()] += words.count(word.lower())
                else:
                    counts[word.lower()] = words.count(word.lower())
    if not counts:
        return
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")
    after = post.name
    count_words(subreddit, word_list, reddit, counts, after=after)
    
