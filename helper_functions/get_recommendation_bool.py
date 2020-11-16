def get_recommendation_bool(df_row):
    """
    Return the Boolean value corresponding to the recommendation.
    """
    rec_bool = None
    if df_row['recommended'] == 'yes':
        rec_bool = True
    elif df_row['recommended'] == 'no':
        rec_bool = False
    else:
        rec_bool = None
    return rec_bool