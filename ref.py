# twitterbot

import io
import sys
import requests
import json


# Make the same request we did earlier, but with the coordinates of San Francisco instead.
parameters = {"lat": 37.78, "lon": -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Get the response data as a python object.  Verify that it's a dictionary.
data = response.json()

print(data["request"]["passes"])

---

import tweepy
import os
import time

consumer_key = ''
consumer_token = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)    
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

os.chdir('images')

for image in os.listdir('.'):
  api.update_with_media(image)
time.sleep(20)

sauce:
https://medium.com/datadriveninvestor/how-i-created-a-twitter-bot-using-python-a68b917d133
