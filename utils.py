import tweepy
import io
import json
import os
import random

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


class StreamListener(tweepy.StreamListener):

    api = None
    
    def setApi(self, api):
        self.api = api
        
    def on_data(self, data):
        data = json.loads(data)

        #make a list so we can the size for upper limit random
        img = os.listdir("./images")
        img = "./images/" + img[random.randint(0, len(img))]

        message = "@" + data["user"]["screen_name"] \
            + " Have a random animal! Beep " \
            + str(random.randint(1e6, 2e6))
        replyid = data["id_str"]
        
        self.api.update_with_media(img, message, replyid)

    def on_error(self, status):
        print("Error: " + str(status))
