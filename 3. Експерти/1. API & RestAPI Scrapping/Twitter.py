# модули: tweepy, TwitterAPI, twython
# user: valerinca
# app: SDP20
Twitter_API_key='y2qgrvwJumCgcUZEe94vF2rfJ'
Twitter_API_secret_key='76XwDEljJRMqU2dkBLHHCNgH1ucvgokvxSBN8FPJXccXaEw6Jr'
Twitter_Bearer_token='AAAAAAAAAAAAAAAAAAAAAKv1KgEAAAAAU7RkSekBdFj5uIrDcMeFmSL3KKc%3DKdLjP1ybQIgYoYhOmUZ5KChlIKVzAdjVWDdjnQ8ah37zg5Mszo'
Twitter_Access_token='181853745-NXtV5bDnLyg1ljWyzwnZdSGJcsN2xZR737L5QCUa'
Twitter_Access_token_secret='IrJIZuJXeKf6gxtUtYSZkhrxW2vLFG7bDi4wNAGTtx9yC'

# Достъп до личния профил
import tweepy
import datetime
#Add your credentials here
twitter_keys = {'consumer_key': Twitter_API_key, 'consumer_secret': Twitter_API_secret_key,
'access_token_key': Twitter_Access_token,'access_token_secret':Twitter_Access_token_secret}
#Setup access to API
auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])
api = tweepy.API(auth)
#Make call on home timeline, print each tweets text
public_tweets = api.home_timeline()
followship=api.followers()
myfriends=api.friends()

for tweet in public_tweets:
    print(tweet.text)
    print()
print(followship)
import json
status = public_tweets[0]
#convert to string
json_str = json.dumps(status._json)
#deserialise string into python object
parsed = json.loads(json_str)
prs2dic=json.dumps(parsed, indent=4, sort_keys=True)
print(prs2dic)


# ********** STREAMING DATA CONTINUEOUSLY
# from tweepy.streaming import StreamListener, Stream
# class Listener ( StreamListener ):
#     def on_status( self, status ):
#         print ('-' * 20)
#         print (status.text)
#         return
# if __name__ == "__main__":
#     listener = Listener()
#     stream = Stream(auth, listener )
#     stream.filter( track=( "Covid", ) )


# Анализ на тутове чрез класове
class TweetMiner(object):
    result_limit = 20
    data = []
    api = False
    Twitter_API_key = 'y2qgrvwJumCgcUZEe94vF2rfJ'
    Twitter_API_secret_key = '76XwDEljJRMqU2dkBLHHCNgH1ucvgokvxSBN8FPJXccXaEw6Jr'
    Twitter_Bearer_token = 'AAAAAAAAAAAAAAAAAAAAAKv1KgEAAAAAU7RkSekBdFj5uIrDcMeFmSL3KKc%3DKdLjP1ybQIgYoYhOmUZ5KChlIKVzAdjVWDdjnQ8ah37zg5Mszo'
    Twitter_Access_token = '181853745-NXtV5bDnLyg1ljWyzwnZdSGJcsN2xZR737L5QCUa'
    Twitter_Access_token_secret = 'IrJIZuJXeKf6gxtUtYSZkhrxW2vLFG7bDi4wNAGTtx9yC'
    witter_keys = {'consumer_key': Twitter_API_key, 'consumer_secret': Twitter_API_secret_key,
                   'access_token_key': Twitter_Access_token, 'access_token_secret': Twitter_Access_token_secret}
    # twitter_keys = {'consumer_key': '---YOUR-KEY---', 'consumer_secret': '---YOUR-KEY---', 'access_token_key': '---YOUR-KEY---', 'access_token_secret': '---YOUR-KEY---' }
    def __init__(self, keys_dict=twitter_keys, api=api, result_limit = 20):
        self.twitter_keys = keys_dict
        auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
        auth.set_access_token(keys_dict['access_token_key'], keys_dict['access_token_secret'])
        self.api = tweepy.API(auth)
        self.twitter_keys = keys_dict
        self.result_limit = result_limit

    def mine_user_tweets(self, user="POTUS", mine_rewteets=False, max_pages=5): # President of US
        data=[]
        last_tweet_id = False
        page = 1
        while page <= max_pages:
            if last_tweet_id:
                statuses = self.api.user_timeline(screen_name=user,count = self.result_limit, max_id = last_tweet_id - 1, tweet_mode = 'extended', include_retweets = True)
            else:
                statuses= self.api.user_timeline(screen_name=user, count=self.result_limit,tweet_mode='extended', include_retweets=True)
            for item in statuses:
                mined = {'tweet_id': item.id,
                'name': item.user.name, 'screen_name': item.user.screen_name, 'retweet_count': item.retweet_count, 'text': item.full_text,
                'mined_at': datetime.datetime.now(), 'created_at': item.created_at, 'favourite_count': item.favorite_count, 'hashtags': item.entities['hashtags'], 'status_count': item.user.statuses_count, 'location': item.place,
                'source_device': item.source }
                try:
                    mined['retweet_text'] = item.retweeted_status.full_text
                except:
                    mined['retweet_text'] = 'None'
                try:
                    mined['quote_text'] = item.quoted_status.full_text
                    mined['quote_screen_name'] = status.quoted_status.user.screen_name
                except:
                    mined['quote_text'] = 'None'
                    mined['quote_screen_name'] = 'None'
                last_tweet_id = item.id
                data.append(mined)
                page += 1
        return data

print('***********************************************')
print('***********************************************')
test=TweetMiner() # пускане и логване
retw=test.mine_user_tweets() # извличане на ретуитнатите поостове
for i in retw:
    print(retw)

import facepy
from facepy import GraphAPI
FB_access_token='EAAKBuZCOri88BAGUmcTgtfLCwxZBYlMRKMkfTtuk0HzQr7KDRETJ9Wr1zIhUuKxmTpHK9KQZCnMyewyjsoRU7jKPXdZAyz0IHf6LUKyxFjKFp1Opct7KD2GKn6l3gSfnDAjZCBwvmGqsuWUkxo3UK6MQPwuYrQqbrXSg2oli1ey6FO0AfsQDM8AjIUpfUZBLjqO8pkabbqcwPK5dgErDbYBr0xDNaFrwZBHDXEWjs3xfF6BTOdUXEoP'
graph = GraphAPI(FB_access_token)
# Кои са последните ми публикации
test_1=graph.get('/me/posts')

# t=graph.get('')
print(test_1)
# Публикуване на снимка
graph.post(path = 'me/photos',source = open('snimka.jpg'))
# Make a FQL query
# graph.fql('SELECT name FROM user WHERE uid = me()') # Make a FQL multiquery
# print(test_1)
# rsvp_status='SELECT uid, rsvp_status FROM event_member WHERE eid=12345678'
# details='SELECT name, url, pic FROM profile WHERE id IN (SELECT uid FROM #rsvp_status)'
# graph.fql({'rsvp_status': rsvp_status,'details': details})
# print(test_2)