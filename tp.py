
import tweepy
from tweepy.streaming import StreamListener, Stream
from tweepy.auth import OAuthHandler
from tweepy.api import API
from datetime import timedelta

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
ACCESS_TOKEN = ''
ACCESS_SECRET = ''
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

class AbstractedlyListener(StreamListener):
    def on_status(self, status):
        status.created_at += timedelta(hours=9)
        #print(u"{text}".format(text=status.text))
        #print(u"{name}({screen}) {created} via {src}\n".format(
    #        name=status.author.name, screen=status.author.screen_name,
    #        created=status.created_at, src=status.source))
        if status.author.screen_name=='Kuske':
            api.retweet(status.id)
            api.create_favorite(status.id)

if __name__ == '__main__':
    stream = Stream(auth, AbstractedlyListener(), secure=True)
    stream.userstream()
    #public_tweets=api.home_timeline()
#python3 tp.py
