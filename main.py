import praw
import utils.config
import pandas as pd
import utils.models as models

import utils.compare as compare
from utils.red import Reddit
import time

def get_friends(user, red):
    user_data_df = models.load_df(store_name="user_data")
    user_data = red.get_user_content(user)#wiinkme #red.get_user(user)


    # user_data = pd.DataFrame()
    # user_data['user'] = ['Zmini12']
    # user_data['subs'] = [{'AskReddit': 0.48514851485148514, 'RocketLeague': 0.039603960396039604, 'RocketLeagueExchange': 0.019801980198019802, 'interestingasfuck': 0.0297029702970297, 'gifs': 0.019801980198019802, 'reflex': 0.019801980198019802, 'woahdude': 0.009900990099009901, 'teenagers': 0.16831683168316833, 'GlobalOffensive': 0.019801980198019802, 'CringeAnarchy': 0.04950495049504951, 'videos': 0.04950495049504951, 'Brogress': 0.009900990099009901, 'talesfromsecurity': 0.009900990099009901, 'longboarding': 0.019801980198019802, 'justneckbeardthings': 0.0297029702970297, 'facepalm': 0.019801980198019802}]
    # user_data['categories'] = [{'meme': 0, 'default': 3, 'porn': 0, 'political': 0, 'cool': 0, 'educational': 0}]

    if user_data is not None and user_data_df is not None:
        # print(dict(pd.DataFrame(user_data)))
        friend, score, common_subreddits, common_categories = compare.compare(user_data_df, user_data.iloc[0])

        # print("You should be friends with %s because you guys had a score of %s. Your common subreddits are %s, your common categories are %s"%(friend['user'], score, common_subreddits, common_categories))
        # print(dict(friend))
        # print(dict(user_data))
        return friend, score, common_subreddits, common_categories

    else:
        print('user is bad')
        return None

def main():
    red = Reddit()

    while True:
        print('getting mentions...')
        # mentions = red.get_mentions(limit=100)
        # print(mentions)
        # for mention in mentions:
        for mention in red.reddit.inbox.stream():
            friend, score, common_subreddits, common_categories = get_friends(mention.author, red)

            mention.reply("You should be friends with /u/%s because you guys had a score of %s. Your common subreddits are %s, your common categories are %s\n\nI am a bot, here is my m̶a̶s̶t̶e̶r̶'̶s̶ coding slave's repository https://github.com/MarcDAFrame/Reddit-Friendship-Service"%(friend['user'], int(score), ', '.join(common_subreddits), ', '.join(common_categories)))

            # print(friend)
            # print(score)
            # print(common_subreddits)
            # print(common_categories)


        time.sleep(5)


main()
