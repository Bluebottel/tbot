#twitter bot

import os
import sys
import tweepy
import utils
import random
from time import sleep
from datetime import datetime

TIME_RETRY_CONNECT = 5

if not len(sys.argv) == 3 or sys.argv[2][0] != "@":
    print("Usage: python3 " + sys.argv[0] + " authfile.txt @username")
    quit()

print("Beep! Twitterbot started.")

tokens = utils.readauthfile(sys.argv[1])
accountname = sys.argv[2]

consumer_key = tokens[0]; consumer_token = tokens[1]
access_token = tokens[2]; access_token_secret = tokens[3]

auth = tweepy.OAuthHandler(consumer_key, consumer_token)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

listener = utils.StreamListener()
listener.setApi(api)
listener.setAccountName(accountname)

stream = tweepy.Stream(auth, listener)
listener.setStream = stream

while True:
    try:
        # this is blocking and starts the actual listening
        stream.filter(track=[sys.argv[2]])
    except KeyboardInterrupt:
        print("Manual stop")
        break
    except e:
        print(e, ": Restarting")
        
    sleep(TIME_RETRY_CONNECT)
    
print("Done")
