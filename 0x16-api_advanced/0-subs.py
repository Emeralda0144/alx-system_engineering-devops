#!/usr/bin/python3
'''
    Queries the Reddit API and returns total
    subscribers of a given subreddit.
'''


def number_of_subscribers(subreddit):
    '''
        Returns the number of subscribers for a given subreddit.
    '''
    from requests import get

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0

    try:
        json = response.json()

    except ValueError:
        return 0

    data = json.get('data')

    if data:
        subscribers = data.get('subscribers')
        if subscribers:
            return subscribers

    return 0