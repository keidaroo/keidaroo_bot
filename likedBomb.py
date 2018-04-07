
import datetime
import random
from datetime import timedelta

import tweepy
from tweepy.api import API
from tweepy.auth import OAuthHandler
from tweepy.streaming import Stream, StreamListener

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


if __name__ == '__main__':
    st = 'liked爆撃開始。 ' + str(datetime.datetime.now())
    api.update_status(st)
    print(st)
    target = 'Vane11ope'
    c = tweepy.Cursor(api.user_timeline, id=target)
    count = 0
    for status in c.items():
        s = status.text
        if('RT'in s or s[0] is '@'):
            continue
        if not status.favorited:
            api.create_favorite(status.id)
        else:
            break
        count += 1
        if(count >= 100):
            break
    st = target + 'さんのツイートを' + str(count) + '件いいねしました。' + str(datetime.datetime.now())
    print(st)
    api.update_status(st)
