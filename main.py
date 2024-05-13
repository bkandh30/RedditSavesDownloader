#Note: This script works for both saved posts and not comments

import praw
from typing import Final
import os
from dotenv import load_dotenv
import logging
import warnings
import csv

warnings.filterwarnings('ignore')

#load our env file
load_dotenv()
client_id: Final[str] = os.getenv('CLIENT_ID')
client_secret: Final[str] = os.getenv('CLIENT_SECRET')
username: Final[str] = os.getenv('USERNAME')
password: Final[str] = os.getenv('PASSWORD')

#set up logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

#Create a reddit instance
reddit = praw.Reddit(
    client_id= client_id,
    client_secret= client_secret,
    user_agent=True,
    username= username,
    password= password,
)
logger.info("Reddit Instance Created")

#Open the csv file
with open('savedPosts.csv','w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['ID', 'Name', 'Subreddit', 'Type', 'URL', 'NoSFW'])
    #Iterate through all the posts
    for link in reddit.user.me().saved(limit=None):
        subreddit = link.subreddit.display_name
        permalink = link.permalink
        # url builder
        post_url = "https://www.reddit.com/" + str(link)
        post_webpage = reddit.submission(url=post_url)
        if isinstance(link, praw.models.Submission):
            title = post_webpage.title
            noSFW = str(link.over_18)
            link_type = "#POST"
        else:
            title = link.submission.title
            noSFW = str(link.submission.over_18)
            link_type = "#COMMENT"
        csv_writer.writerow([title, subreddit, permalink, link_type, noSFW])

logger.info("All the saved posts from the reddit account are available in the file")