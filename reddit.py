''' Made by Guilherme Moreira, used on the twitter account @RedditHotNews '''

import praw, twitter
from keys import *
from time import sleep
from datetime import datetime


reddit = praw.Reddit(client_id = client_id,
                     client_secret = client_secret,
                     user_agent = 'r/news forwarder') #reddit api wrapper

subreddit = reddit.subreddit('news') #subreddit selector, the one which the posts are going to be selected from

api = twitter.Api(consumer_key = consumer_key,
                  consumer_secret = consumer_secret,
                  access_token_key = access_token_key,
                  access_token_secret = access_token_secret,
                  sleep_on_rate_limit = True) #twitter api wrapper


def getSubmission():
    for submission in subreddit.hot(limit=10): #goes through the 10 hottest posts in r/news
        if submission.score >= 1000 and submission.url != None: #checks the amount of upvotes and if the post has a link
            try:
                short = 'redd.it/{}'.format(submission.id) #makes a redd.it shortlink using the submission id
                api.PostUpdate("{title}, {shortLink} {url}".format(title = submission.title, shortLink = short, url = submission.url)) #tweets
                print(submission.id)
            except:
                print('duplicate')
while 1:
    print('start at {}'.format(datetime.now()))
    getSubmission()
    print('sleep')
    sleep(600) #sleeps  for 10 min
