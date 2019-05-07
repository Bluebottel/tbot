import tweepy
import io
import json

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

        #m = "@username textmessage"
        #t = api.update_status(status=m,
        # in_reply_to_status_id=tweet.id)
        
        print("data: " + data["text"])

        self.api.update_status("Reply to " + \
                          data["user"]["screen_name"])

    def on_error(self, status):
        print("Error: " + str(status))
