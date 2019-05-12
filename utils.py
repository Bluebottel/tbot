import tweepy
import io
import json
import os
import random
import time
import datetime

SLEEP_TIME_RATE = 60 * 5
SLEEP_TIME_SERVERS = 30

def readauthfile(filename):
    """ order of keys
    consumer_key
    consumer_token
    access_token
    access_token_secret
    """
    tokens = []

    file = io.open(filename, mode="r", encoding="utf-8")

    for line in file:
        # chop off the newline
        tokens.append(line[:-1])

    return tokens

def findkeywords(message):
    words = []

    

class StreamListener(tweepy.StreamListener):

    api = None; accountname = None; time = None
    
    def setApi(self, api):
        self.api = api

    def setAccountName(self, name):
        self.accountname = name
        
    def on_data(self, data):
        data = json.loads(data)
        
        img = os.listdir("./images")        
        img = "./images/" + img[random.randint(0, len(img))]
        
        message = "@" + data["user"]["screen_name"] \
            + " Have a random animal! Beep " \
            + str(random.randint(1e6, 2e6))
        replyid = data["id_str"]
        
        # replying to ourselves causes infinite posting loops
        if data["user"]["screen_name"] != self.accountname:
            self.api.update_with_media(img, message, replyid)

    def on_error(self, status):

        # unauthorized error
        if status == 401:
            print("Error 401 (unauthorized). Possibly broken keys")
            quit()

        # getting rate limited so pause posting
        elif status == 420 or 429:
            time.sleep(SLEEP_TIME_RATE)

        # gateway timeout or internal server error
        # the servers are up but try again later
        elif status == 504 or status == 500:
            time.sleep(SLEEP_TIME_SERVERS)

        else:
            print("Error: %s", status)
            quit()
