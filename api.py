import tweepy
import json
import datetime

# Twitter scraper - user_timeline scraping via API.

# Following block of code contains 4 params: first two consumer keys, two other app tokens
# Together they are used to authorize our app via Twitter API

consumer_key = 'X'
consumer_secret_key = 'X'
access_token = 'X'
access_token_secret = 'X'

# This block uses tweepy authentication methods to combine tokens from above.
# Uses API tweepy method to connect with API

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# This block uses tweepy method to get public tweets from our own timeline and prints in console.


def get_my_tweets():
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)
    print('did it')

# This block returns user_account metadata (such as user_name, user_followers_count, followed_names).


def get_my_metadata():
    user = api.get_user('AdrianTrzoss')
    print(user.screen_name)
    print(user.followers_count)
    for friend in user.friends():
        print(friend.screen_name)

# This function returns to json given user's tweets from timeline (specified number of recent tweets).
# For iteration selects certain attributes from tweet_class and creates new tweets adding them to new empty 2d_list


def get_user_tweets():
    timeline_tweets = []
    user_name = input('Please give the username: ')
    number_of_tweets_to_get = int(input('How many tweets you would like to get?: '))
    get_tweets = api.user_timeline(screen_name=user_name, count=number_of_tweets_to_get, tweet_mode="extended")
    timeline_tweets.extend(get_tweets)
    output_tweets = []
    for t in timeline_tweets:
        output_tweet = [t.id_str, t.created_at, t.full_text, t.source, t.retweet_count, t.favorite_count, t.retweeted]
        output_tweets.append(output_tweet)
    return output_tweets, user_name


# Function output to json saves return from ger user tweets to json file.


def output_tweets_to_json(output_tweets, user_name):
    dict_b = {}
    for i in range(len(output_tweets)):
        dict_b[i] = {
            'id': output_tweets[i][0],
            'created_at': output_tweets[i][1],
            'full_text': output_tweets[i][2],
            'source': output_tweets[i][3],
            'retweet_count': output_tweets[i][4],
            'favorite_count': output_tweets[i][5],
            'isretweeted': output_tweets[i][6]
        }
    filename = '{}.json'.format(user_name)
    with open(filename, 'w') as f:
        json.dump(dict_b, f, indent=4, default=str)


# main function aggregates collection public tweets from user's page.

def main():
    output_tweets, user_name = get_user_tweets()
    output_tweets_to_json(output_tweets, user_name)
    print('Wykonano')


if __name__ == '__main__':
    main()
