
import praw
import os
from dotenv import load_dotenv,dotenv_values
load_dotenv()

reddit_instance = praw.Reddit(
    client_id = os.getenv("client_id"),
    client_secret = os.getenv("client_secret"),
    username = os.getenv("USER_NAME"),
    password = os.getenv("password"),
    user_agent="test_bot"
)
subreddit = reddit_instance.subreddit("nba")

#get hot posts from reddit
hot_posts = subreddit.hot(limit=5)
for i in hot_posts:
    print(i.title)
    
# top_month = subreddit.top(limit = 5, time_filter = "month")
# print("#####")
# for i in top_month:
#     print(i.title)


#submit to reddit

#subreddit.submit(title="my first test post from bot", selftext="Hello my name is AnthonyBot")

#get comments from a post

# submission = reddit_instance.submission("1c2bd36")
# comments = submission.comments
# for i in comments:
#     if "guy" in i.body:
#         print(i.body)

