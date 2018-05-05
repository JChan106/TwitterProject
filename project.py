from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import sys
import ssl
import json
import urllib.request as urllib2
from bs4 import BeautifulSoup

arguments = sys.argv[3:]
filename = sys.argv[1]
numtweets = int(sys.argv[2])

soup = BeautifulSoup(urllib2.urlopen("https://www.google.com"), "html.parser")
print(soup.title.string)

print(filename)

keywords = ' '.join(arguments)

print(keywords)

#consumer key, consumer secret, access token, access secret.
ckey="5QVnDuXPag3EKOrjre2YRZNcm"
csecret="6k97AOJWD7vgtS2Ndq3sUmZWvUPBkMW1MXLI7L6nE7H8h4KsNJ"
atoken="815885741108494336-ooTId5Ha5QVsywP8TXOqSieZdBJE3Id"
asecret="nAuuwvhPwxbn5gMqJZgXuviMdPpxoeqgSxjmzWFPVEa2S"


class listener(StreamListener):
    counttweets = 0
    def on_data(self, data):
        # tweet = data.split(',"text":"')[1].split('","source')[0]
        with open(filename, 'a') as the_file:
            if self.counttweets < numtweets:
                # the_file.write('tweet: ' +tweet+'\n')
                the_file.write(data)
                self.counttweets+=1
                print(self.counttweets)
            else:
                print("hi")
                sys.exit()
        return(True)

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=arguments)
