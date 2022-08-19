import tweepy
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

response = client.get_tweets(id="id_example_here")

print(response.data.text)