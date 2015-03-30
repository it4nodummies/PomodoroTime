__author__ = 'IT4noDummies'


import threading

from twython import Twython


APP_KEY = '8TmMkuHDZRZ4MuWbtbIelGstP'
APP_SECRET = 'qMD6FEgnVauH6zMmAAFZeCrQwXofCWcpCkv3tXP0DTrPADaDtb'
OAUTH_TOKEN = '3114767247-KAEHsjeYXzn1OiMzUeyicxOgh9R92PAlW273ASC'
OAUTH_TOKEN_SECRET = '6QibPwpiRAL1127eJjeRcll3D80usfR1JCt0uBGAMqbmG'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# print twitter.verify_credentials()

time_line =  twitter.get_home_timeline()

for i in time_line:
    print i

# twitter.update_status(status='See how easy using Twython is!')
print " "

mentions =  twitter.get_mentions_timeline()



for dic in mentions:
    print dic['user']
    print dic.keys()
    print dic['text']

    print dic['user'].keys()
    print dic['user']['screen_name']
    print dic['created_at']



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
