import praw

import config

print(config.client_id, config.client_secret, config.user_agent)

reddit = praw.Reddit(username=config.username, 
                    password=config.password,
                    client_id=config.client_id,
                    client_secret=config.client_secret,
                    user_agent=config.user_agent)

# for submission in reddit.subreddit('test').hot(limit=10):
#     print(submission.title)


for mention in reddit.inbox.mentions(limit=25):
    # print('{}\n{}\n'.format(mention.author, mention.body))
    print(dir(mention.author))
    m = mention.author
    # print(m.downvoted)
    # print(m.upvoted)
    # print(m.stream)
    for post in m.upvoted.top():
        print(post)
    print(dir(m.upvoted))
