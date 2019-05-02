#twitter bot


import io
import sys
import requests
import tweepy
import json
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

print(tokens)
