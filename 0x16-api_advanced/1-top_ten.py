#!/usr/bin/python3
'''
    Prints titles of the first 10 hot posts
    for a given subreddit.
'''


def top_ten(subreddit):
    '''
        Prints titles of the first 10 hot posts
        for a given subreddit.
    '''
    import requests
    import sys

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        req = requests.get(url, headers=headers, allow_redirects=False)
        if req.status_code == 200:
            req = req.json()
            for post in req['data']['children'][:10]:
                print(post['data']['title'])
        else:
            print(None)
    except Exception:
        print(None)