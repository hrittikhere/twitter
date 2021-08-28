import tweepy
from time import sleep


CONSUMER_KEY = 'XXXX'
CONSUMER_SECRET = 'XXXX'
ACCESS_KEY = 'XXXX'
ACCESS_SECRET = 'XXXX'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)

url="https://twitter.com/your_username/status/" ##USE YOUR USER NAME

for status in tweepy.Cursor(api.search, q=('portainer'), lang='en').items(20):
            try:
                a=status.id
                print(url+str(a))
            except Exception:
                print()
 
