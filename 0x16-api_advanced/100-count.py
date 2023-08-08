#!/usr/bin/python3
"""
100-count
"""

import requests

def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.

    Args:
        subreddit (str): The subreddit name to query.
        word_list (list): List of keywords to count.
        after (str): The 'after' parameter for pagination (default=None).
        word_count (dict): Dictionary to store keyword counts (default={}). 

    Returns:
        None
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'my-app/0.1'}  # Set a custom User-Agent
    params = {'after': after} if after else None

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                if f' {word.lower()} ' in f' {title} ':
                    word_count[word] = word_count.get(word, 0) + 1

        after = data['data']['after']
        if after is not None:
            return count_words(subreddit, word_list, after=after, word_count=word_count)
        else:
            sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_word_count:
                print(f'{word}: {count}')
    else:
        return None

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = sys.argv[2:]
        count_words(subreddit, word_list)
