import tweepy

chave_consumidor = 'xxxxxxx'
segredo_consumidor = 'xxxxxxx'
token_acesso = 'xxxxxxx'
token_acesso_segredo = 'xxxxxxx'

api_key = ''
api_key_secret = ''
bearer_token = ''


if __name__ == '__main__':
    auth = tweepy.OAuth2BearerHandler(bearer_token)
    api = tweepy.API(auth)
    results = api.search_tweets(q='COVID-19', count=100)

    users = []
    tweets = []
    for tweet in results:
        users.append(tweet.user.name)
        tweets.append(tweet.text)

        print(f'User: {tweet.user.name} | Location {tweet.user.location} | aTweet: {tweet.text} ')

    print('executing data collection')