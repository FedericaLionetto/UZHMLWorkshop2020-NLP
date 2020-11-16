import numpy as np
import pandas as pd
import datetime as dt

def get_review_date_date_flown_distance_days(df_row):
    """
    Return the time distance in days from the date flown to the review date.
    """
    review_date_date_flown_distance_days = None
    if (df_row['review_date_timestamp'] is None or df_row['date_flown_timestamp'] is None or df_row['review_date'] == pd.NaT or df_row['date_flown'] == pd.NaT or df_row['review_date_timestamp'] == np.NaN or df_row['date_flown_timestamp'] == np.NaN or str(df_row['review_date_timestamp']) == 'NaT' or str(df_row['date_flown_timestamp']) == 'NaT'):
        review_date_date_flown_distance_days = None
    else:
        # print(df_row['review_date_timestamp'])
        # print(df_row['date_flown_timestamp'])
        # review_date_flown_distance = dt.datetime.fromtimestamp(df_row['review_date_timestamp'])-dt.datetime.fromtimestamp(df_row['date_flown_timestamp'])
        review_date_date_flown_distance = df_row['review_date_timestamp']-df_row['date_flown_timestamp']
        review_date_date_flown_distance_days = review_date_date_flown_distance.days
    return review_date_date_flown_distance_days