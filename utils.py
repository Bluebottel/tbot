import tweepy
import io
import json
import os
import random
import time
from datetime import datetime
import re

SLEEP_TIME_RATE = 60 * 5
SLEEP_TIME_SERVERS = 30
KEYWORDS_FILE = "keywords.json"

def readauthfile(filename):
    """ order of keys
    consumer_key
    consumer_token
    access_token
    access_token_secret
    """
    tokens = []

    with open(filename, mode="r", encoding="utf-8") as file:
        for line in file:
            # chop off the newline and += doesn't work here
            tokens.append(line[:-1])

    return tokens

def scrubmessage(message):

    # strip out all non alphabetical characters and spaces
    message = re.sub('[^A-Za-z ]', '', message)

    message = message.lower()
    message = message.split(" ")
    
    return message    

def loadjsonfile(path):

    tags = ""
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                tags += line
    except OSError:
        print("Error opening file ", path)
        return None
    try:
        # make it a dict
        tags = json.loads(tags)
    except:
        print("Broken JSON in " + path)
        return None

    return tags

# find keywords in the received message
def keywordsinmessage(message):
    
    keywords = getkeywords(); found = []
    message = scrubmessage(message)

    for word in message:
        if word in keywords:
            found.append(word)

        # simple singular form check (pups -> pup)
        elif word[:-1] in keywords:
            found.append(word[:-1])
    return found

# reads from a file since dbless branch, JSON formatted
def getkeywords():

    tags = loadjsonfile(KEYWORDS_FILE)

    # the values are the keywords
    allwords = []
    for keys, value in tags.items():
        for tag in value:
            if tag not in allwords:
                allwords.append(tag)

    return allwords
    

class StreamListener(tweepy.StreamListener):

    api = None; accountname = None; stream = None
    
    def setApi(self, api):
        self.api = api

    def setAccountName(self, name):
        self.accountname = name

    def setStream(self, stream):
        self.stream = stream
        
    def on_data(self, data):
        data = json.loads(data)

        # you don't strictly need to @ a user to reply
        message = "@" + data["user"]["screen_name"] + " "
        
        
        # get keywords that are mentioned in the tweet
        keywords = keywordsinmessage(data["text"])

        images = loadjsonfile(KEYWORDS_FILE)
        
        # if no keywords were mentioned just pick among all keywords
        if (keywords == None or keywords == []):
            message += "Have a random animal!"

        # if one or more pick a random one of those
        else:
            chosen = random.choice(keywords)
            message += "Have a " + chosen + "!"

            # create a list where only images tagged with the chosen
            # keywords are included
            images = [k for k,v in images.items() if chosen in v]
            

        message += " Beep " + str(random.randint(1e6, 2e6))
        img = random.choice(list(images))
        replyid = data["id_str"]
        
        # replying to ourselves causes an infinite posting loop
        # this will get you banned from twitter
        if data["user"]["screen_name"] != self.accountname:
            self.api.update_with_media(img, message, replyid)

    def on_error(self, status):

        # unauthorized error
        if status == 401:
            print("Error 401 (unauthorized). Possibly broken keys")
            stop_stream(self.stream)
            quit()

        # getting rate limited so pause posting
        elif status == 420 or 429:
            time.sleep(SLEEP_TIME_RATE)

        # gateway timeout or internal server error
        # the servers are up but try again later
        elif status == 504 or status == 500:
            time.sleep(SLEEP_TIME_SERVERS)

        else:
            print("Error: ", status)
            quit()
