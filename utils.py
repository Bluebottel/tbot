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

    # make it lowercase
    message = message.lower()

    # split into words
    message = message.split(" ")
    return message    

def extractkeywords(message):
    keywords = getkeywords(); found = []
    message = scrubmessage(message)

    for word in message:
        if word in keywords:
            found.append(word)

        # also check for the singular version of the word (pups -> pup)
        elif word[:-1] in keywords:
            found.append(word[:-1])

    return found

# reads from a file since dbless branch, JSON formatted
def getkeywords():
    ret = ""

    try:
        with open(KEYWORDS_FILE, "r", encoding="utf-8") as file:
            for line in file:
                ret += line[:-1]
    except OSError as wrongfile:
        print("Error opening file " + KEYWORDS_FILE)
        return None

    try:
        # make it a pythonised list
        ret = json.loads(ret)
    except:
        print("Broken JSON in " + KEYWORDS_FILE)
        return None

    # the values are the keywords
    allwords = []
    for keys, value in ret.items():
        for tag in value:
            if tag not in allwords:
                allwords.append(tag)

    return allwords
    

class StreamListener(tweepy.StreamListener):

    api = None; accountname = None;
    
    def setApi(self, api):
        self.api = api

    def setAccountName(self, name):
        self.accountname = name
        
    def on_data(self, data):
        data = json.loads(data)
        
        img = os.listdir("./images")        
        img = "./images/" + img[random.randint(0, len(img))]

        """" TODO
        message = "@" + data["user"]["screen_name"] \
            + " Have a random animal! Beep " \
            + str(random.randint(1e6, 2e6))
        replyid = data["id_str"]
        """

        keywords = getkeywords(data["text"])

        if (keywords != None or keywords != []):
            pass #TODO
        
        
        # replying to ourselves causes an infinite posting loop
        # this will get you banned from twitter
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
