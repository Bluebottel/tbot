#twitter bot

import sys
import tweepy
import utils

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


listener = utils.StreamListener()
listener.setApi(api)

stream = tweepy.Stream(auth, listener)

# this is blocking and starts the actual listening
#stream.filter(track=["@wasdmuraibot"])



print("Done")
