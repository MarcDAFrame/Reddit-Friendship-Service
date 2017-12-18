import time


def assign_score(obj1, obj2):
    score = 0
    common_subreddits = []
    common_categories = []
    # print(type(obj1), type(obj2))
    # print(obj1['user'], obj2['user'])
    if obj1['user'] != obj2['user']:
        for key, value in obj1['subs'].items():
            if key in obj2['subs'].keys():
                common_subreddits.append(key)
                d = abs(int(obj1['subs'][key]*100) - int(obj2['subs'][key]*100))
                if d == 0:
                    score += 100
                else:
                    score += 50/d
        # print(type(obj2['categories']))
        for key, value in obj1['categories'].items():
            if key in obj2['categories'].keys() and obj1['categories'][key] != 0 and obj2['categories'][key] != 0:
                common_categories.append(key)
                d = abs(int(obj1['categories'][key]*100) - int(obj2['categories'][key]*100))
                if d == 0:
                    score += 100
                else:
                    score += 50/d
        
        # print(score)
        return score, common_subreddits, common_categories
    return 0, [], []
    

def compare(df, obj):
    """
    compare(DataFrame, dict) -> pd.Series, float
    goes through list of all
    """

    max_score, common_subreddits, common_categories = assign_score(df.iloc[0], obj)

    friend = None
    friend_categories = None
    friend_subreddits = None
    start = time.time()
    
    for i in range(1, len(df.index)):

        current_score, common_subreddits, common_categories = assign_score(df.iloc[i], obj)
        if  current_score > max_score:
            max_score = current_score
            friend = df.iloc[i]
            friend_subreddits = common_subreddits
            friend_categories = common_categories
            # print(common_subreddits, common_categories, friend['user'])


    print("time elapsed: ", time.time() - start)
    return friend, max_score, friend_subreddits, friend_categories

