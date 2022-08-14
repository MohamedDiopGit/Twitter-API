# import the module
import tweepy

# assign the values accordingly


# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# set access to user's access key and access secret
auth.set_access_token(access_token, access_token_secret)

# calling the api
api = tweepy.API(auth)
# the screen_name of the targeted user
user = api.get_users_following("")


 
# printing the latest 20 followers of the user
# for follower in api.followers(screen_name):
# 	print(follower.screen_name)

print('Latest Followers:')
for follower in user.followers():
    print('Name: ' + str(follower.name))
    print('Username: ' + str(follower.screen_name))