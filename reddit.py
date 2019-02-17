''' Made by Guilherme Moreira, used on the twitter account @RedditHotNews '''

import praw, twitter
from keys import *
from datetime import datetime


api = twitter.Api(consumer_key = consumer_key,
                  consumer_secret = consumer_secret,
                  access_token_key = access_token_key,
                  access_token_secret = access_token_secret,
                  sleep_on_rate_limit = True) #twitter api wrapper


def getSubmission():

    reddit = praw.Reddit(client_id = client_id,
                         client_secret = client_secret,
                         user_agent = 'r/news forwarder') #reddit api wrapper

    subreddit = reddit.subreddit('news') #subreddit selector, the one which the posts are going to be selected from

    for submission in subreddit.hot(limit=20): #goes through the 10 hottest posts in r/news
        if submission.score >= 1000 and submission.url != None: #checks the amount of upvotes and if the post has a link
            try:
                short = 'redd.it/{}'.format(submission.id) #makes a redd.it shortlink using the submission id
                api.PostUpdate("{title}, {shortLink} {url}".format(title = submission.title, shortLink = short, url = submission.url)) #tweets
                print(submission.id)
            except: #an error will arise if the reddit post has already been posted
                print('duplicate')

print('start at {}'.format(datetime.now()))
getSubmission()
print('end at {}'.format(datetime.now()))
