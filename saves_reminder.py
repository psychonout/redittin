from datetime import datetime
from random import choice

import praw
import requests

from config import settings

reddit = praw.Reddit(
    client_id=settings.reddit_client_id,
    client_secret=settings.reddit_client_secret,
    username=settings.reddit_username,
    password=settings.reddit_password,
    user_agent=settings.reddit_user_agent,
)

saved_reddit_items = [item for item in reddit.user.me().saved(limit=None)]

item = choice(saved_reddit_items)

message = f"""{item.title} saved at {datetime.fromtimestamp(item.created_utc)}

{item.url}"""

print(message)

requests.post(settings.slack_webhook, json={"text": message}, timeout=10)

item.unsave()
