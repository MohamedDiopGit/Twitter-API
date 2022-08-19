import tweepy
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

# check 
# https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query
# OR
# https://github.com/twitterdev/getting-started-with-the-twitter-api-v2-for-academic-research/blob/main/modules/5-how-to-write-search-queries.md
# for specified quieries

query = 'text_example -is:retweet'  

# check : 
# https://developer.twitter.com/en/docs/twitter-api/expansions
# and https://developer.twitter.com/en/docs/twitter-api/fields
# for more expansions and fields
response = client.search_all_tweets(query=query, max_results=10, tweet_fields=['created_at', 'lang'], user_fields=['profile_image_url'], expansions=['author_id'])


users = {user['id']:user for user in response.includes['users']}
# print(response)

for tweet in response.data:
    if users[tweet.author_id] :
        user = users[tweet.author_id]
        print(user.username)
        print("id: ",tweet.id)
        print("text: ",tweet.text)
        print("lang:",tweet.lang)
print(len(response.data))