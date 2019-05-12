#twitter bot

import os
import sys
import tweepy
import utils
import random

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

# this is blocking and starts the actual listening
stream.filter(track=[sys.argv[2]])

# TODO: handle read timeouts exception when connection breaks(?)
# google fu: read timeout tweepy

print("Done")
