import praw
import utils.config as config
from utils.classify import Classifier
import pandas as pd
import time
import copy
def sort_dict(di):
    li = []
    for key, value in sorted(di.items(), key=lambda kv: (-kv[1], kv[0])):
        li.append((key, value))
    return li

class Reddit():
    def __init__(self):
        self.reddit = praw.Reddit(username=config.username,
                            password=config.password,
                            client_id=config.client_id,
                            client_secret=config.client_secret,
                            user_agent=config.user_agent)

        self.classifier = Classifier()

    def get_user_content(self, user):
        """
        (<praw redditor>)-> dict
        """
        try:
            df = pd.DataFrame(columns=['user'])
            temp_subreddits = {}
            pos = 0
            neg = 0
            count = 0

            comments = user.comments.new(limit=101)

            # print("==========user==========")
            # print(str(user))
            for post in comments:
                count += 1

                if str(post.subreddit) in temp_subreddits.keys():
                    temp_subreddits[str(post.subreddit)] += 1
                else:
                    temp_subreddits[str(post.subreddit)] = 1


                # a, b = self.classifier.classify_text(str(post.body))
                # pos += a
                # neg += b


            if count < 100:
                return None

            # if len(temp_subreddits) < 5:
            #     return None

            subreddits = {}
            for sub in temp_subreddits.keys():
                subreddits[sub] = temp_subreddits[sub]/count

            temp_categories = {}
            for sub_category in config.sub_categories.keys():
                temp_categories[sub_category] = len(config.sub_categories[sub_category] & set(temp_subreddits.keys()))


            # df['pos'] = [pos/count]
            # df['neg'] = [neg/count]
            # df['count'] = [count]

            df['user'] = [str(user)]
            df['subs'] = [subreddits]
            df['categories'] = [temp_categories]


            return df
        except Exception as e:
            print(str(e))
            return None


    def get_users(self, limit=100):
        # subreddits = ['funny', 'pics', 'cringeanarchy', 'politics', 'aww']
        authors = set([])
        # print('+'.join(subreddits))
        for post in self.reddit.subreddit('all').new(limit=limit): #'+'.join(subreddits)).new(limit=limit)
            authors.add(post.author)

        return authors

    def parse_mentions(self, mentions):
        for m in mentions:
            self.get_user_content(m.author)

    def get_user(self, username):
        return self.reddit.redditor(username)