__author__ = 'IT4noDummies'

import threading

import twitter

from config import *

api = twitter.Api(consumer_key=APP_KEY, consumer_secret=APP_SECRET, access_token_key=OAUTH_TOKEN, access_token_secret=OAUTH_TOKEN_SECRET)

mentions = api.GetMentions()

if len(mentions) > 15:
    mentions = mentions[:15]
for tweet in mentions:
    print '@'+tweet.user.screen_name+': '
    print tweet.GetText()
    print tweet.GetCreatedAt()

tweets = api.GetHomeTimeline()

if len(tweets) > 15:
    tweets = tweets[:15]
for tweet in tweets:
    print '@'+tweet.user.screen_name+': '
    print tweet.GetText()



TOTAL = 0
MY_LOCK = threading.RLock()


class CountThread(threading.Thread):
    def run(self):
        global TOTAL
        for i in range(100000):
            MY_LOCK.acquire()
            TOTAL += 1
            MY_LOCK.release()
        print('%s\n' % TOTAL)

a = CountThread()
b = CountThread()
