import utils.models as models
import time
from utils.classify import Classifier
from utils.red import Reddit
import pandas as pd


def main():
    red = Reddit()

    # start = time.time()

    user_data_df = models.load_df(store_name="user_data")

    users = red.get_users(limit=10000)
    count = 0 
    for user in users:
        user_data = red.get_user_content(user) #reddit.redditor("TheC4T")
        # print("user_data", user_data)
        if user_data is not None:
            # print("dataframe", pd.DataFrame(user_data, index=[0]))
            if user_data_df is not None:
                user_data_df = user_data_df.append(user_data, ignore_index=True)
            else:
                user_data_df = user_data
        
        else: #if the user doesn't get conte55.7175901766nt
            print('FAIL')
            pass 
        
        count+=1
        print(count)
    
    #after it as finished iterating
    user_data_df = user_data_df.drop_duplicates(subset='user', keep="last")

    print(models.save_df(user_data_df, store_name="user_data"))
    # print("time elapsed:", time.time()-start)
main()

# user_data_df = models.load_df(store_name="user_data")

# print(user_data_df)

# print(len(users), users)