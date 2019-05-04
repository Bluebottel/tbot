#twitter bot


import io
import sys
import requests
import tweepy
import utils

""" order of keys
consumer_key
consumer_token
access_token
access_token_secret
"""

if not len(sys.argv) == 2:
    print("Usage: python3 " + sys.argv[0] + " authfile.txt")
    quit()

print("Beep! Twitterbot started.")

tokens = utils.readauthfile(sys.argv[1])

consumer_key = tokens[0]; consumer_token = tokens[1]
access_token = tokens[2]; access_token_secret = tokens[3]

auth = tweepy.OAuthHandler(consumer_key, consumer_token)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
#api.update_status('Beep! Bot update #1')

print("Done")

