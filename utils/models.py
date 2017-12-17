import pandas as pd

store = pd.HDFStore('./saves/store.h5')

# store['df'] = df  # save it
# store['df']  # load it


def save_df(df, store_name='user_data'):
    # print(df)
    try:
        store['user_data'] = df
    except Exception as e:
        print(e)
        return False
    else:
        return True
    
def load_df(store_name="user_data"):
    try:
        return store.get('user_data')
    except KeyError: #it doesn't exist yet
        pass


# save_df(pd.DataFrame({"test" : [1,2,3]}))

# print(load_df())