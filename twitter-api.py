# import the module
import tweepy
import config

# authorization of consumer key and consumer secret

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)
 
users = client.get_users_followers(id=config.USER_ID)

for user in users.data:
    print(user.keys)
    #print(user.username)  #for instance
 
print("Number of followers displayed: ",len(users.data))