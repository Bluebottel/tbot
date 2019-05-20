# tbot
A twitter bot that replies with pictures of cute animals. It will establish a connection to the twitter
streaming API and trigger the on_data event when it gets a mention. 

*Dependencies*

Tweepy - https://github.com/tweepy/tweepy

*Usage*
main authfile @username

The authfile should contain the twitter API keys in the following order:
consumer_key

consumer_token

access_token

access_token_secret

They are generated on your twitter dashboard > apps > your_app > keys and tokens. The @username can
anything really as long as it's accepted by the twitter API as a valid search request.

Note that twitter doesn't really like bots doing whatever they want in general so many replies will
go missing for no apparent reason. It helps if the mentioner is following you and, if that also fails,
persistence.
